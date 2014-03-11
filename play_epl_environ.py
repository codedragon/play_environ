# cringe #
from pandaepl.common import *
from environment import Environment


class playEnviron:
    def __init__(self):
        """
        Initialize the experiment
        """
        # Get experiment instance.
        print 'init'
        exp = Experiment.getInstance()
        exp.setSessionNum(0)
        config = Conf.getInstance().getConfig()  # Get configuration dictionary.

        print config['terrainModel']
        # Load environment
        self.environ = Environment(config)
        test = base.cam.node().getLens()
        print test
        print test.getFov()
        print test.getAspectRatio()
        print 'camera position', base.cam.getPos()
        print 'near camera', test.getNear()

    def start(self):
        """
        Start the experiment.
        """
        #print 'start'
        Experiment.getInstance().start()

if __name__ == '__main__':
    #print 'main?'
    playEnviron().start()
else:
    print 'not main?'


