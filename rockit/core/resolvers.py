import logging

from rest_framework.reverse import reverse_lazy

class CommandResolver(object):
    """
    Helper for resolving commands, used specific patterns on each command to determine
    how to resolve it. E.g command type 
    """
    logger = logging.getLogger(__name__)

    def __init__(self):
        # All currently supported command
        self._supportedCommands = {
            'binary': lambda r,n,c: self._resolve_command_binary(r,n,c)
        }

    def resolve_commands(self, request, node_id, commands):
        """
        Keywords arguments:

        request  - request object used for reverse lookup
        node_id  - current node id
        commands - all commands to be resolved
        """
        if commands:
            unsupported = list()
            for command in commands['commands']:
                if command['type'] in self._supportedCommands:
                    self._supportedCommands[command['type']](request, node_id, command)
                else:
                    unsupported.append(command.type)
        else:
            self.logger.debug("Could not resolve comamnds, commands are empty")

        return commands

    def _resolve_command_binary(self, request, node_id, command):
        urls = dict()

        cid = command['id']
        on  = command['values']['on']
        off = command['values']['off']

        urls['on']  = reverse_lazy('commands-set', kwargs={ 'pk': node_id, 'cid': cid, 'value': on }, request=request)
        urls['off'] = reverse_lazy('commands-set', kwargs={ 'pk': node_id, 'cid': cid , 'value': off }, request=request)
        urls['current'] = reverse_lazy('commands-get', kwargs={ 'pk': node_id, 'cid': cid }, request=request)

        command['urls'] = urls
