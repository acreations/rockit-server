from rest_framework import viewsets

from rockit.plugins.mailout import models
from rockit.plugins.mailout import serializers

class NodeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows node categories to be view and set
    """
    queryset = models.Node.objects.all()
    serializer_class = serializers.NodeSerializer