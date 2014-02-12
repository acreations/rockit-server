import logging

from rockit.plugins.razberry import models

logger = logging.getLogger(__name__)

class RazberryParser(object):

    def __init__(self):
        self._supportedCommandClasses = {
            '37':  True, # SwitchBinary
            '39':  True, # SwitchAll
            '50':  True, # Meter
            '114': True, # ManufacturerSpecific
            '134': True, # Version
            '129': True, # Clock
            '138': True, # Time
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
            '133': True, # Association
            '143': True, # MultiCmd
            '152': True, # Security
        }

    def parseDevices(self, devices):
        if devices:
            for key,device in devices.items():
                data = device['data']
                node, created = models.Node.objects.get_or_create(device_id=key)

                node.device_type = self._getValue(data['deviceTypeString'])

                node.manufacturer_id   = self._getValue(data['manufacturerId'])
                node.manufacturer_name = self._getValue(data['vendorString'])

                node.listening = self._getValue(data['isListening'])
                node.routing = self._getValue(data['isRouting'])
                node.awaken = self._getValue(data['isAwake'])
                node.failed = self._getValue(data['isFailed'])

                node.beaming = self._getValue(data['beam'])

                self._parseInstances(node, device['instances'])

            return len(devices.keys())

        return None

    def _getValue(self, data, defaultValue=""):
        if data and data['value']:
            return data['value']
        return defaultValue

    def _parseCommandClasses(self, node, commandClasses):
        if node and commandClasses:            
            for key in commandClasses:
                unknown = list()

                if key in self._supportedCommandClasses:
                    logger.debug(commandClasses[key])
                elif key in self._ignoredCommandClasses:
                    pass
                else:
                    unknown.append(key)
        else:
            logger.warn("Cannot parse command classes, node or command classes are empty")


    def _parseInstances(self, node, instances):
        if node and instances:
            for key, instance in instances.items():
                self._parseCommandClasses(node, instance['commandClasses'])
        else:
            logger.warn("Cannot parse instances, node or instances are empty")