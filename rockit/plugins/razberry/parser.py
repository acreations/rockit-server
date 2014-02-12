import logging

from rockit.plugins.razberry import models

logger = logging.getLogger(__name__)

class RazberryParser(object):

    def parseDevices(self, devices):
        if devices:
            for key,device in devices.items():
                data = device['data']
                node, created = models.Node.objects.get_or_create(device_id=key)

                node.device_type = self._getValue(data['deviceTypeString'])
                node.device_name = self._getValue(data[''])

                node.manufacturer_id   = self._getValue(data['manufacturerId'])
                node.manufacturer_name = self._getValue(data['vendorString'])

                node.listening = self._getValue(data['isListening'])
                node.routing = self._getValue(data['isRouting'])
                node.awaken = self._getValue(data['isAwake'])
                node.failed = self._getValue(data['isFailed'])

    frequent_listening = models.BooleanField(default = False)
                node.beaming = self._getValue(data['beam'])
    security = models.BooleanField(default = False)

                print self._getValue(data['isRouting'])

            return len(devices.keys())

        return None

    def _getValue(self, data, defaultValue=""):
        if data and data['value']:
            return data['value']
        return defaultValue