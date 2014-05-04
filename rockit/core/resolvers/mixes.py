import logging

from rest_framework.reverse import reverse_lazy

class MixesResolver(object):
    logger = logging.getLogger(__name__)

    def __init__(self):
        # All currently supported command
        self.resolves = {
            'when': lambda r,c: self.resolve_when(r,c),
            'then': lambda r,c: self.resolve_then(r,c),
            'finish': lambda r,c: self.resolve_finish(r,c)
        }

    def resolve_mixes(self, request, content):
        """
        Resolve mixes (when, then, finish)
        """

        if content:
            for key in content:
                if key in resolves:
                    self.resolves[key](request, content[key])

        return content

    def resolve_finish(self, request, content):
        pass

    def resolve_then(self, request, content):
        pass

    def resolve_when(self, request, content):
        pass