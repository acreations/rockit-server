from rest_framework import viewsets

from rockit.core import models
from rockit.core import serializers

class ScheduleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows schedule to be view.

    """
    queryset = models.Schedule.objects.all()
    serializer_class = serializers.ScheduleSerializer