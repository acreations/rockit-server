from celery.execute import send_task

from rest_framework import viewsets
from rest_framework.response import Response

from rockit.core import models
from rockit.core import holders

class WhenViewSet(viewsets.ViewSet):
    """
    View to list all addable nodes in rockit server.
    """
    def list(self, request):
        """
        Return a list of all addables.
        """
        result = holders.Holder()

        for a in models.Association.objects.all():
            task = send_task("%s.when" % a.entry, args=[holders.WhenHolder(a)])
            when = task.wait(timeout=30)
            
            if when:
                result.extend(when)

        return Response(result.get_content())