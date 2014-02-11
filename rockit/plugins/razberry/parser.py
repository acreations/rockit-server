import logging

logger = logging.getLogger(__name__)

class RazberryParser(object):

    def parseDevices(self, devices):
        if(devices):
            for key,device in devices.items():
                print device['data']['name']

        return None
