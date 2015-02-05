from celery.execute import send_task

from django.shortcuts import get_object_or_404

from rest_framework.response import Response
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

    def update(self, request, pk=None):
        action = get_object_or_404(self.queryset, pk=pk)

        then = models.ActionThen.objects.filter(holder=action)

        for item in then:
            t = send_task("%s.mixes.then.run" % item.target.entry, [item.identifier])
            value = t.wait(timeout=15)

        return Response({'success':True})