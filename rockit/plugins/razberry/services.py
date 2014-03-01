import logging
import requests

from rockit.plugins.razberry import constants
from rockit.plugins.razberry import models

class RazberryService(object):

    logger = logging.getLogger(__name__)

    SERVICE_URI  = "http://%s/%s"
    SERVICE_DATA = "ZWaveAPI/data/%s"
    SERVICE_GET  = "ZWaveAPI/run/%s"
    SERVICE_SET  = "ZWaveAPI/run/%s.Set(%s)"

    def data(self, timestamp=0):
        return self._send_request(self.SERVICE_DATA % timestamp)

    def retrieve(self, namespace):
        if namespace:
            return self._send_request(self.SERVICE_GET % namespace)
        else:
            self.logger.debug("Cannot retrieve, namespace is empty")
        return None

    def retrieve_instances(self, device_id):
        return self.retrieve("devices.%s.instances" % device_id)

    def update(self, namespace, value):
        if namespace and value:
            normalized_value = value

            if bool(value):
                normalized_value = str(value).lower()

            return self._send_request(self.SERVICE_SET % (namespace, normalized_value))
        else:
            self.logger.debug("Cannot update, namespace or value is empty")

        return None

    def normalize(self, namespace):
        if namespace:
            splits = namespace.split(".")
            result = list()

            for current in splits:
                if current.isdigit():
                    last_seen = result[-1]

                    if 'commandClasses' in last_seen:
                        result[-1] = last_seen + "[%s]" % hex(int(current))
                    else:
                        result[-1] = last_seen + "[%s]" % current
                else:
                    result.append(current)
            return '.'.join(result)
        else:
            self.logger.debug("Could not normalize, namespace is empty")

        return namespace

    def _send_request(self, path):
        server_address = SettingsService().get(constants.SETTING_SERVER_ADDRRESS)
        
        self.logger.debug("Razberry server address %s" % server_address)
        self.logger.debug("Request: %s"  % path)

        if server_address and path:
            normalized = self.normalize(path)
            r = requests.get(self.SERVICE_URI % (server_address, normalized))
            return r.json()
        else:
            self.logger.debug("Server address is not set yet")
        return None

class SettingsService(object):
    """
    Settings service is used to get all settings for Razberry plugin. 
    Here will also be able to add caching, failsafe lookups etc
    """

    def get(self, key, default=None):
        try:
            return models.Setting.objects.get(name=key).value
        except models.Setting.DoesNotExist:
            return default