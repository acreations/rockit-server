from rest_framework import viewsets

from rockit.core import models
from rockit.core import serializers

class ActionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows actions to be view and set. 

    """
    queryset = models.Action.objects.all()
    serializer_class = serializers.ActionSerializer