from celery.execute import send_task

from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from rockit.core import models
from rockit.core import serializers
from rockit.core import tasks

class ActionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows actions to be view and set.

    """
    queryset = models.Action.objects.all()
    serializer_class = serializers.ActionSerializer

    def destroy(self, request, pk=None):
        instance = self.get_object()

        self._notify_plugins(models.ActionThen.objects, instance, 'mixes.then.destroy')

        return super(ActionViewSet, self).destroy(request, pk)

    def update(self, request, pk=None):
        """
        Send a notification to update plugins
        """
        instance = self.get_object()

        self._notify_plugins(models.ActionThen.objects, instance, 'mixes.then.run')

        return Response({'success': True})

    def _notify_plugins(self, models, instance, notification):
        """
        Notify plugins
        """
        for item in models.filter(holder=instance):
            t = send_task("%s.%s" % (item.target.entry, notification), [item.identifier])
            v = t.wait(timeout=15)


