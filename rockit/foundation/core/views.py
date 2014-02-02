from rest_framework import viewsets

from rockit.foundation.core import models
from rockit.foundation.core import serializers

from rest_framework.reverse import reverse_lazy

class AssociationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows nodes to be view and set. 

    """
    queryset = models.Association.objects.all()
    serializer_class = serializers.AssociationSerializer