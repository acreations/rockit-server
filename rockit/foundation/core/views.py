from celery.execute import send_task

from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy
from rest_framework.views import APIView

from rockit.foundation.core import models
from rockit.foundation.core import serializers
from rockit.foundation.core.holders.commands import CommandsHolder
from rockit.foundation.core.holders.details import DetailsHolder
from rockit.foundation.core.holders.settings import SettingsHolder

import logging

logger = logging.getLogger(__name__)

class AddableViewSet(viewsets.ViewSet):
    """
    View to list all addable nodes in rockit server.
    """
    def list(self, request):
        """
        Return a list of all addables.
        """
        result = list()
        for association in models.Association.objects.filter(addable=True):
            result.append({
                'name': association.name,
                'url':  reverse_lazy("%snode-list" % association.entry, request=request)
                })
        return Response(result)

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

        task_c = send_task("%s.node.commands" % node.association.entry, args=[node.id, CommandsHolder()])
        commands = task_c.wait(timeout=30)

        response.data['commands'] = commands.get_content()
        response.data['detailed'] = detailed.get_content()

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