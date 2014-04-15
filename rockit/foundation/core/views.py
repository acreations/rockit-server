from celery.execute import send_task

from django.shortcuts import get_object_or_404


from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy
from rest_framework.views import APIView

from rockit.foundation.core import models
from rockit.foundation.core import serializers
from rockit.foundation.core.holders.commands import CommandsHolder
from rockit.foundation.core.holders.details import DetailsHolder
from rockit.foundation.core.holders.settings import SettingsHolder
from rockit.foundation.core.holders.when import WhenHolder
from rockit.foundation.core import resolvers

import logging

logger = logging.getLogger(__name__)

class ActionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows actions to be view and set. 

    """
    queryset = models.Action.objects.all()
    serializer_class = serializers.ActionSerializer

class AssociationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows association to be view and set. 

    """
    queryset = models.Association.objects.all()
    serializer_class = serializers.AssociationSerializer

class CommandRetrieveViewSet(generics.RetrieveAPIView):
    """
    API endpoint for setting and getting a specific command
    """
    serializer_class = serializers.NodeSerializer

    def retrieve(request, *args, **kwargs):
        queryset = models.Node.objects.all()
        node     = get_object_or_404(queryset, pk=kwargs['pk'])

        retrieve = send_task("%s.node.command.value" % node.association.entry, kwargs={
            'identifier': node.aid,
            'command_id': kwargs['cid']
            })
        value = retrieve.wait(timeout=30)

        if value:
            return Response({ 'data': value })

        return Response({ 'detail': 'Not found' }, status=status.HTTP_404_NOT_FOUND)

class CommandUpdateViewSet(generics.RetrieveAPIView):
    """
    API endpoint for setting and getting a specific command
    """
    serializer_class = serializers.NodeSerializer

    def retrieve(request, *args, **kwargs):
        queryset = models.Node.objects.all()
        node     = get_object_or_404(queryset, pk=kwargs['pk'])
        
        update = send_task("%s.node.command.update.value" % node.association.entry, kwargs={
            'identifier': node.aid,
            'command_id': kwargs['cid'],
            'value': kwargs['value']
            })
        value = update.wait(timeout=30)

        if value is not None:
            return Response({ 'data': value })

        return Response({ 'detail': 'Not found' }, status=status.HTTP_404_NOT_FOUND)

    def update(request, *args, **kwargs):
        queryset = models.Node.objects.all()
        node     = get_object_or_404(queryset, pk=kwargs['pk'])

        return Response(kwargs['value'])

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

        task_d = send_task("%s.node.detailed" % node.association.entry, args=[node.id, DetailsHolder()])
        detailed = task_d.wait(timeout=30)

        if not task_d.failed():
            response.data['detailed'] = detailed.get_content()

        task_c = send_task("%s.node.commands" % node.association.entry, args=[node.id, CommandsHolder()])
        commands = task_c.wait(timeout=30)

        if not task_c.failed():
            resolver = resolvers.CommandResolver()
            response.data['commands'] = resolver.resolve_commands(request, pk, commands.get_content())

        return response

class SettingViewSet(viewsets.ViewSet):
    """
    View to list all settings in rockit server.
    """

    def list(self, request):
        """
        Return a list of all settings.
        """
        result = list()
        for association in models.Association.objects.all():
            result.append({
                'name': association.name,
                'url':  reverse_lazy("setting-detail", kwargs={ 'pk': association.id }, request=request)
                })

        return Response(result)

    def retrieve(self, request, pk=None):
        """
        Get settings for a specific association
        """
        queryset = models.Association.objects.all()
        association = get_object_or_404(queryset, pk=pk)

        settings = send_task("%s.settings" % association.entry, args=[SettingsHolder()])
        result = settings.wait()

        return Response(result.get_content())

class WhenViewSet(viewsets.ViewSet):
    """
    View to list all addable nodes in rockit server.
    """
    def list(self, request):
        """
        Return a list of all addables.
        """
        result = WhenHolder()

        result.add('1', 'Alarm')

        return Response(result.get_content())