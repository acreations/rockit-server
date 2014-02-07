from rest_framework import viewsets

from rockit.plugins.mailout import models
from rockit.plugins.mailout import serializers

class NodeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows node categories to be view and set
    """
    queryset = models.MailoutNode.objects.all()
    serializer_class = serializers.NodeSerializer

class ServerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows node categories to be view and set
    """
    queryset = models.MailoutServer.objects.all()
    serializer_class = serializers.ServerSerializer