import logging

class ActionBuilder(object):
    """
    This builder encapsulate rockit holder in order to produce a action response
    """

    logger = logging.getLogger(__name__)

    def __init__(self, commandClasses):
        self.commandClasses = commandClasses 

        self.supported = {
            '37': lambda h, c: self._generalize_switch_binary(h, c),
        }

    def filter_actions_by_command_classes(self, device_id, holder):
        """
        Get all filtered out action for a specific device
        """
        if device_id and holder:   
            unsupported = list()
            unsupported_razberry = list()

            for key in self.commandClasses:
                command = self.commandClasses[key]
                if not command['supported']:
                    unsupported_razberry.append(command)
                elif key in self.supported:
                    self.supported[key](holder, command)
                else:
                    unsupported.append({ 'name': command['name'], 'value': key })

            if unsupported:
                self.logger.debug("Unsupported commandClasses in builder %s" % unsupported)

            if unsupported_razberry:
                self.logger.debug("Unsupported commandClasses in builder (razberry) %s" % unsupported_razberry)
        else:
            self.logger.warn("Cannot parse command classes, node or holder are empty")

        return holder

    def _generalize_switch_binary(self, holder, command):
        holder.add_switch_command(
            command['id'], 
            command['name'],
            255, 0,
            command['data']['level']['value'])