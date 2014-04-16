from rest_framework import viewsets
from rest_framework.response import Response

from rockit.foundation.mixes import holders

class WhenViewSet(viewsets.ViewSet):
    """
    View to list all addable nodes in rockit server.
    """
    def list(self, request):
        """
        Return a list of all addables.
        """
        result = holders.WhenHolder()

        result.add('1', 'Alarm')

        return Response(result.get_content())