import logging

import requests

from rockit.plugins.razberry import constants
from rockit.plugins.razberry import models

class RazberryService(object):

    logger = logging.getLogger(__name__)

    SERVICE_DATA = "http://%s/ZWaveAPI/data/%s"
    SERVICE_GET  = "http://%s/ZWaveAPI/run/%s.Get()"
    SERVICE_SET  = "http://%s/ZWaveAPI/run/%s.Set(%s)"

    def data(self, timestamp=0):
        server_address = SettingsService().get(constants.SETTING_SERVER_ADDRRESS)

        if server_address:
            service = self.SERVICE_DATA % (server_address, timestamp)

            r = requests.get(service)

            return r.json()
        else:
            self.logger.debug("Server address is not set yet")
        return None

    def retrieve(self, namespace):
        pass

    def update(self, namespace, value):
        pass

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


class CommandClassesService(object):

    logger = logging.getLogger(__name__)

    def retrieve(self):
        pass

    def generate_commands(self):
        pass


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