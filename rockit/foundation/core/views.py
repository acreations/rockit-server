from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from rockit.foundation.core import models
from rockit.foundation.core import serializers

from rest_framework.reverse import reverse_lazy

class AssociationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows nodes to be view and set. 

    """
    queryset = models.Association.objects.all()
    serializer_class = serializers.AssociationSerializer

class SettingsViewSet(viewsets.ViewSet):
    """
    View to list all settings in rockit server.

    This includes all plugins which got its own settings, the rockit server will just point to it
    using reverse lookup.
    """

    def list(self, request):
        """
        Return a list of all settings.
        """
        result = list()

        for association in models.Association.objects.all():
            result.append({
                'name': association.name,
                'url': reverse_lazy('%s-settings' % association.entry, request=request)
            })

        return Response(result)

class Settings(APIView):
    """
    View to list settings in rockit server. (No plugins settings here)
    """

    def get(self, request, format=None):
        """
        Return a list of settings
        """
        return Response("TEST")
