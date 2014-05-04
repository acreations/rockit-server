from celery.execute import send_task

from rest_framework import viewsets
from rest_framework.response import Response

from rockit.core import models
from rockit.core import holders

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
                result.extend(mixes)

        return Response(result.get_content())