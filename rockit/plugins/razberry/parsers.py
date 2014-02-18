import logging

from rockit.plugins.razberry import constants as c
from rockit.plugins.razberry import models

class RazberryParser(object):

    def __init__(self):
        self.logger = logging.getLogger(__name__)

        self._supportedCommandClasses = {
            '134': lambda n,k,c: self._parse_node_version(n,k,c) 
        }

        self._ignoredCommandClasses = {
            '37':  True, # SwitchBinary
            '39':  True, # SwitchAll
            '32':  True, # Basic
            '38':  True, # SwitchMultilevel
            '34':  True, # ApplicationStatus
            '43':  True, # SceneActivation
            '49':  True, # SensorMultilevel
            '50':  True, # Meter
            '70':  True, # ClimateControlSchedule
            '96':  True, # MultiChannel
            '112': True, # Configuration
            '114': True, # ManufacturerSpecific
            '119': True, # NodeNaming
            '129': True, # Clock
            '133': True, # Association
            '138': True, # Time
            '143': True, # MultiCmd
            '152': True, # Security
        }

    def parse_command_classes(self, node, commandClasses):
        if node and commandClasses:   
            unknownClass = list()

            for key in commandClasses:
                if key in self._supportedCommandClasses:
                    self._supportedCommandClasses[key](node, key, commandClasses[key]['data'])
                else:
                    unknownClass.append({ 'name': commandClasses[key]['name'], 'value': key })
            if unknownClass:
                self.logger.debug("Unsupported commandClasses %s" % unknownClass)
        else:
            self.logger.warn("Cannot parse command classes, node or command classes are empty")

    def parse_devices(self, devices):
        result = list()

        if devices:
            for key, device in devices.items():
                data = device['data']

                node, created = models.Node.objects.get_or_create(device_id=key)

                node.device_type = self._get_value(data['deviceTypeString'])
                node.manufacturer_id   = self._get_value(data['manufacturerId'])
                node.manufacturer_name = self._get_value(data['vendorString'])

                node.listening = self._get_value(data['isListening'])
                node.routing   = self._get_value(data['isRouting'])
                node.awaken    = self._get_value(data['isAwake'])
                node.beaming = self._get_value(data['beam'])
                node.failed  = self._get_value(data['isFailed'])

                node.save()

                self.parse_instance(node, device['instances'])

                result.append(key)
        else:
            self.logger.debug("Cannot parse devices, devices are empty")

        return result

    def parse_instance(self, node, instances):
        if node and instances:
            for key, instance in instances.items():
                self.parse_command_classes(node, instance['commandClasses'])
        else:
            self.logger.warn("Cannot parse instances, node or instances are empty")

    def _get_value(self, data, defaultValue=""):
        if data and data['value']:
            return data['value']
        return defaultValue

    def _get_value_as_version(self, minor, major, defaultValue=""):
        if(minor and major):
            result = "%s.%s" % (self._get_value(minor), self._get_value(major))

            if len(result) is not 1:
                return result
        return defaultValue

    def _parse_node_version(self, node, key, commandClass):
        version, created = models.NodeVersion.objects.get_or_create(node=node)

        version.sdk = self._get_value(commandClass['SDK'])

        version.application = self._get_value_as_version(
            commandClass['applicationMajor'], commandClass['applicationMinor'])

        version.zw_library  = self._get_value(commandClass['ZWLib'], 0)
        version.zw_protocol = self._get_value_as_version(
            commandClass['ZWProtocolMajor'], commandClass['ZWProtocolMinor'])

        version.save()
