from rest_framework import viewsets

from rockit.core import models
from rockit.core import serializers

class AssociationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows association to be view and set. 

    """
    queryset = models.Association.objects.all()
    serializer_class = serializers.AssociationSerializer