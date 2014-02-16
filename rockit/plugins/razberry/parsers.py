import logging

from rockit.plugins.razberry import constants as c
from rockit.plugins.razberry import models

class RazberryParser(object):

    def __init__(self):
        self.logger = logging.getLogger(__name__)

        self._supportedCommandClasses = {
            c.CLASS_SWITCH_BINARY: lambda n,k,c: self._parseNodeCommand(n,k,c),
            #'39':  True, # SwitchAll
            #'50':  True, # Meter
            #'114': True, # ManufacturerSpecific
            c.CLASS_VERSION:  lambda n,k,c: self._parseNodeVersion(n,k,c) 
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

    def parseDevices(self, devices):
        if devices:
            result = list()

            for key,device in devices.items():
                data = device['data']
                node, created = models.Node.objects.get_or_create(device_id=key)

                node.device_type = self._getValue(data['deviceTypeString'])

                node.manufacturer_id   = self._getValue(data['manufacturerId'])
                node.manufacturer_name = self._getValue(data['vendorString'])

                node.listening = self._getValue(data['isListening'])
                node.routing   = self._getValue(data['isRouting'])
                node.awaken    = self._getValue(data['isAwake'])
                node.failed = self._getValue(data['isFailed'])

                node.beaming = self._getValue(data['beam'])

                self._parseInstances(node, device['instances'])

                node.save()
                
                result.append(key)

            return result

        return None

    def _getValue(self, data, defaultValue=""):
        if data and data['value']:
            return data['value']
        return defaultValue

    def _getValueAsVersion(self, minor, major, defaultValue=""):
        if(minor and major):
            result = "%s.%s" % (self._getValue(minor), self._getValue(major))

            if len(result) is not 1:
                return result
        return defaultValue

    def _parseCommandClasses(self, node, commandClasses):
        if node and commandClasses:   
            unknownClass = list()

            for key in commandClasses:
                if key in self._supportedCommandClasses:
                    self._supportedCommandClasses[key](node, key, commandClasses[key]['data'])
                elif key in self._ignoredCommandClasses:
                    pass
                else:
                    unknownClass.append(key)

            if unknownClass:
                self.logger.debug("Unsupported commandClasses %s" % unknownClass)
        else:
            self.logger.warn("Cannot parse command classes, node or command classes are empty")

    def _parseInstances(self, node, instances):
        if node and instances:
            for key, instance in instances.items():
                self._parseCommandClasses(node, instance['commandClasses'])
        else:
            self.logger.warn("Cannot parse instances, node or instances are empty")

    def _parseNodeCommand(self, node, key, commandClass):
        pass

    def _parseNodeVersion(self, node, key, commandClass):
        version, created = models.NodeVersion.objects.get_or_create(node=node)

        version.sdk = self._getValue(commandClass['SDK'])

        version.application = self._getValueAsVersion(
            commandClass['applicationMajor'], commandClass['applicationMinor'])

        version.zw_library  = self._getValue(commandClass['ZWLib'], 0)
        version.zw_protocol = self._getValueAsVersion(
            commandClass['ZWProtocolMajor'], commandClass['ZWProtocolMinor'])

        version.save()
