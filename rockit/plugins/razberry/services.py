import logging

import requests

from rockit.plugins.razberry import constants
from rockit.plugins.razberry import models

class RazberryService(object):

    logger = logging.getLogger(__name__)

    SERVICE_DATA = "http://%s/ZWaveAPI/data/%s"

    def data(self, timestamp=0):
        server_address = SettingsService().get(constants.SETTING_SERVER_ADDRRESS)

        if server_address:
            service = self.SERVICE_DATA % (server_address, timestamp)

            r = requests.get(service)

            return r.json()
        else:
            logger.warn("Server address is not set yet")
        return None


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