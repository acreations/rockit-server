from celery.execute import send_task

from rest_framework import viewsets
from rest_framework.response import Response

from rockit.foundation.core import models
from rockit.foundation.core.holders.holder import Holder
from rockit.foundation.mixes import holders

class WhenViewSet(viewsets.ViewSet):
    """
    View to list all addable nodes in rockit server.
    """
    def list(self, request):
        """
        Return a list of all addables.
        """
        result = Holder()

        for a in models.Association.objects.all():
            print a.entry
            task = send_task("%s.when" % a.entry, args=[holders.WhenHolder(a.id)])
            when = task.wait(timeout=30)
            print when.get_content()
            result.extend(when)

        return Response(result.get_content())