from rest_framework.reverse import reverse_lazy

from rockit.core import holders
from rockit.core import models

class MixesResolver(object):
 
    def resolve(self, request, holder):
        """
        Resolve names for (when, then, finish)
        """
        assert holder

        self._resolve_url(request, holder.when)
        self._resolve_url(request, holder.then)
        self._resolve_url(request, holder.finish)

        return holder

    def _resolve_url(self, request, container):
        assert container

        association = container['association']

        for item in container['items']:
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


