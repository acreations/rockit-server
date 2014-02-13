from celery.execute import send_task

from rest_framework import viewsets

from rockit.plugins.mailout import models
from rockit.plugins.mailout import serializers

#class NodeViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows node categories to be view and set
#    """
#    queryset = models.MailoutNode.objects.all()
#    serializer_class = serializers.NodeSerializer

#    def create(self, request):
#        response = super(NodeViewSet, self).create(request)

#        create = send_task("rockit.register.node", args=[10, 1])
#        result = create.wait()

#        return response

#class ServerViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows node categories to be view and set
#    """
#    queryset = models.MailoutServer.objects.all()
#    serializer_class = serializers.ServerSerializer