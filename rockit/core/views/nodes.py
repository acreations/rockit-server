from celery.execute import send_task

from django.shortcuts import get_object_or_404

from rest_framework import viewsets

from rockit.core import holders
from rockit.core import models
from rockit.core import resolvers
from rockit.core import serializers

class NodeCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows node categories to be view and set
    """
    queryset = models.NodeCategory.objects.all()
    serializer_class = serializers.NodeCategorySerializer

class NodeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows nodes to be view and set.

    """
    queryset = models.Node.objects.all()
    serializer_class = serializers.NodeSerializer

    def retrieve(self, request, pk=None):
        response = super(NodeViewSet, self).retrieve(request, pk)

        node = get_object_or_404(self.queryset, pk=pk)

        task_d = send_task("%s.node.detailed" % node.association.entry, args=[node.id, holders.DetailsHolder()])
        detailed = task_d.wait(timeout=30)

        if not task_d.failed():
            response.data['details'] = detailed.get_content()['data']['details']

        task_c = send_task("%s.node.commands" % node.association.entry, args=[node.id, holders.CommandsHolder()])
        commands = task_c.wait(timeout=30)

        if not task_c.failed():
            resolver = resolvers.CommandResolver()
            response.data['commands'] = resolver.resolve_commands(request, pk, commands.get_content()['data']['commands'])

        return response