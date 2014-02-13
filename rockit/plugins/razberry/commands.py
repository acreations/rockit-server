import logging

from rockit.plugins.razberry import constants
from rockit.plugins.razberry import models

class CommandsGenerator(object):

    def __init__(self, device_id, holder):
        self.device = models.Node.object.get(device_id=device_id)
        self.holder = holder
        self.logger = logging.getLogger(__name__)

        self._supportedCommandClasses = {
            #'37':  True, # SwitchBinary
            #'39':  True, # SwitchAll
            #'50':  True, # Meter
            #'114': True, # ManufacturerSpecific
            '134':  lambda n, c: self._parseNodeVersion(n, c) # Version
        }

        self._ignoredCommandClasses = {
            '32':  True, # Basic
            '38':  True, # SwitchMultilevel
            '34':  True, # ApplicationStatus
            '43':  True, # SceneActivation
            '49':  True, # SensorMultilevel
            '70':  True, # ClimateControlSchedule
            '96':  True, # MultiChannel
            '112': True, # Configuration
            '119': True, # NodeNaming
            '129': True, # Clock
            '133': True, # Association
            '138': True, # Time
            '143': True, # MultiCmd
            '152': True, # Security
        }

    def generate_commands(self):
        pass
