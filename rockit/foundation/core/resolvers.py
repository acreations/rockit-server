import logging

from rest_framework.reverse import reverse_lazy

class CommandResolver(object):
    """
    Helper for resolving 
    """
    logger = logging.getLogger(__name__)

    def __init__(self):

        self._supportedCommands = {
            'binary': lambda r,p,c: self._resolve_command_binary(r,p,c)
        }

    def resolve_commands(self, request, pk, commands):
        if commands:
            unsupported = list()
            for command in commands['data']:
                if command['type'] in self._supportedCommands:
                    self._supportedCommands[command['type']](request, pk, command)
                else:
                    unsupported.append(command.type)
        else:
            self.logger.debug("Could not resolve comamnds, commands are empty")

        return commands

    def _resolve_command_binary(self, request, pk, command):
        urls = dict()

        cid = command['id']
        on  = command['values']['on']
        off = command['values']['off']

        urls['on']  = reverse_lazy('commands-set', kwargs={ 'pk': pk, 'cid': cid, 'value': on }, request=request)
        urls['off'] = reverse_lazy('commands-set', kwargs={ 'pk': pk, 'cid': cid , 'value': off }, request=request)
        urls['current'] = reverse_lazy('commands-get', kwargs={ 'pk': pk, 'cid': cid }, request=request)

        command['urls'] = urls
