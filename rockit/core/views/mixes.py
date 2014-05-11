from celery.execute import send_task

from rest_framework import viewsets
from rest_framework.response import Response

from rockit.core import models
from rockit.core import holders
from rockit.core import resolvers

class MixesViewSet(viewsets.ViewSet):
    """
    List all addable mix states in rockit server
    """
    def list(self, request):
        """
        Return a list of all addables.
        """
        result = holders.Holder()

        for a in models.Association.objects.all():
            task = send_task("%s.mixes" % a.entry, args=[holders.MixesHolder(a)])
            mixes = task.wait(timeout=30)
            
            if mixes:
                mixes = resolvers.MixesResolver().resolve(request, mixes)
                result.extend(resolvers.MixesNameResolver().resolve(mixes) if mixes.should_resolve_names() else mixes)

        return Response(result.get_content())

    def details(self, request, *args, **kwargs):
        """
        Return specifc options for the requested mix
        """

        entry = kwargs['entry']
        identifier = kwargs['pk']

        task = send_task("%s.mixes.details" % entry, args=[identifier, holders.MixesDetailsHolder()])
        mixes = task.wait(timeout=30)

        return Response(mixes.get_content())