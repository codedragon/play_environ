from direct.showbase.ShowBase import ShowBase
from direct.showbase.DirectObject import DirectObject
from panda3d.core import PerspectiveLens, Point3
from math import pi, sin, cos
from direct.task import Task
import sys
sys.path.insert(1, '../goBananas')
from load_models import load_models
from environment import PlaceModels
from direct.gui.OnscreenImage import OnscreenImage


# Constants
TURN_RATE = 20  


class BananaWorld(DirectObject):
    def __init__(self):
        # this will be in the config file usually
        path_to_models = '../goBananas/'
        # using log.txt in this directory (gobananas), Yummy banana09
        #avatar_head = -23.0306647431 
        #avatar_pos = Point3(-0.499429, 4.01372, 1)
        #banana_pos = Point3(-0.461612, 4.1383, 1)
        #banana_h = 35

        # using giz_bananarchy.txt in this directory Yummy banana4
        avatar_head = 32.6150996909
        avatar_pos = Point3(-2.53202, 3.98558, 1)
        banana_pos = Point3(-2.88193, 4.38051, 1)
        banana_h = -418

        # Things that can affect camera:
        # options resolution resW resH
        base = ShowBase()
        lens = PerspectiveLens()
        # Fov is set in config for 60
        lens.setFov(60)
        # aspectratio should be same as window size
        # this was for 800x600
        # field of view 60 46.8264...
        # aspect ratio 1.3333
        lens.setAspectRatio(800.0 / 600.0)
        base.cam.node().setLens(lens)
        print lens.getFov()
        print lens.getAspectRatio()
        # set near to be same as avatar's radius
        lens.setNear(0.1)
        print 'near camera', lens.getNear()
        #base.cam.setPos(0, 0, 1)
        base.cam.setPos(avatar_pos)
        base.cam.setH(avatar_head)
        #self.smiley = base.loader.loadModel('smiley')
        #self.smiley.setPos(Point3(0, 6, 0))
        #self.smiley.reparentTo(render)
        #print 'smiley', self.smiley.getPos()
        
        # load environment
        load_models()
        for item in PlaceModels._registry:
            if item.group == 'original':
                if item.name is not 'sky':
                    item.model = path_to_models + item.model
                    model = base.loader.loadModel(item.model)
                    model.setPos(item.location)
                    model.setScale(item.scale)
                    model.reparentTo(render)

        sky = base.loader.loadModel('models/sky.egg')
        sky.setPos(0, 0, -10)
        sky.reparentTo(render)
        sky.setHpr(0, 270, 0)
        #b=OnscreenImage(image="models/pics/Mount_Rainier_6874h.jpg")
        #b.parent = base.cam
        #b.scale = (640, 0, 360)
        #b.pos = (20, 20, 10)
        #base.cam.node().getDisplayRegion(0).setSort(20)
        #imageObject = OnscreenImage(image = 'models/pics/Mount_Rainier_6874h.jpg', pos = (-0.5, 0, 0.02))
        #imageObject.parent = camera
        # A dictionary of what keys are curently being pressed
        self.keys = {"right" : 0,
                     "left" : 0}
        self.accept("escape", sys.exit)
        self.accept("arrow_right", self.setKey, ['right', 1])
        self.accept("arrow_left", self.setKey, ['left', 1])
        self.accept("arrow_right-up", self.setKey, ['right', 0])
        self.accept("arrow_left-up", self.setKey, ['left', 0])

        self.playTask = base.taskMgr.add(self.frame_loop, "frame_loop")
        self.playTask.last = 0

    # As described earlier, this simply sets a key in the self.keys dictionary to
    # the given value
    def setKey(self, key, val): self.keys[key] = val
    
    def frame_loop(self, task):
        dt = task.time - task.last
        task.last = task.time
        self.update_camera(dt)

        #angleDegrees = task.time * 10.0
        #angleRadians = angleDegrees * (pi / 180)
        #base.cam.setPos(1 * sin(angleRadians), -1.0 * cos(angleRadians), 2)
        #base.cam.setHpr(angleDegrees, 0, 0)
        
        #self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        #self.camera.setHpr(angleDegrees, 0, 0)

        return task.cont

    def update_camera(self, dt):
        heading = base.cam.getH()  
        pos = base.cam.getPos()
        if self.keys["right"]:
            heading -= dt * TURN_RATE
            base.cam.setHpr(heading, 0, 0)
        elif self.keys["left"]:
            heading += dt * TURN_RATE
            base.cam.setHpr(heading, 0, 0)
                  
       
if __name__ == "__main__":
    BW = BananaWorld()
    run()
