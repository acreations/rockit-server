from rest_framework.reverse import reverse_lazy

from rockit.core import holders
from rockit.core import models

class MixesResolver(object):

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
        assert content

        for key in content:
            if key in self.resolves:
                self.resolves[key](request, content)

        return content

    def resolve_finish(self, request, content):
        assert content and 'finish' in content

        for when in content['finish']:
            association = when['association']

            for item in when['items']:
                item['url'] = reverse_lazy('mixes-details', kwargs={ 'pk': item['identifier'], 'entry': association['entry'] }, request=request)

    def resolve_then(self, request, content):
        pass

    def resolve_when(self, request, content):
        assert content and 'when' in content

        for when in content['when']:
            association = when['association']

            for item in when['items']:
                item['url'] = reverse_lazy('mixes-details', kwargs={ 'pk': item['identifier'], 'entry': association['entry'] }, request=request)

class MixesNameResolver(object):

    def resolve(self, holder):
        """
        Resolve names for (when, then, finish)
        """
        assert holder

        self._resolve_names(holder.when)
        self._resolve_names(holder.then)
        self._resolve_names(holder.finish)

        return holder

    def _resolve_names(self, container):
        assert container

        for item in container['items']:
            if models.Node.objects.filter(aid=item['identifier']).exists():
                node = models.Node.objects.get(aid=item['identifier'])

                item['name'] = node.name


