import logging

class ValueResolver(object):
    """
    Helper for resolving commands value
    """
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.supported = {
            'SwitchBinary': lambda c: "data.level.value"
        }

    def resolve_command_value(self, command):
        """
        Resolve command value
        """
        if command:
            key = command['name']
            if key in self.supported:
                return self.supported[key](command)
            else:
                self.logger.warn('Command not supported, will not resolve')
        else:
            self.logger.warn("Cannot resolve command value, command is empty")

        return None