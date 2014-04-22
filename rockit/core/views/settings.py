from celery.execute import send_task

from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy

from rockit.core.models import Association
from rockit.core.holders import SettingsHolder

class SettingViewSet(viewsets.ViewSet):
    """
    View to list all settings in rockit server.
    """

    def list(self, request):
        """
        Return a list of all settings.
        """
        result = list()
        for association in Association.objects.all():
            result.append({
                'name': association.name,
                'url':  reverse_lazy("setting-detail", kwargs={ 'pk': association.id }, request=request)
                })

        return Response(result)

    def retrieve(self, request, pk=None):
        """
        Get settings for a specific association
        """
        queryset = Association.objects.all()
        association = get_object_or_404(queryset, pk=pk)

        settings = send_task("%s.settings" % association.entry, args=[holders.SettingsHolder()])
        result = settings.wait()

        return Response(result.get_content())