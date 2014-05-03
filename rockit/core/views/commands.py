from celery.execute import send_task

from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from rockit.core import models
from rockit.core import serializers

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
