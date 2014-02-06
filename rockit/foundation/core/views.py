from celery.execute import send_task

from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy
from rest_framework.views import APIView

from rockit.foundation.core import models
from rockit.foundation.core import serializers
from rockit.foundation.core.holders.settings import SettingsHolder

class AssociationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows nodes to be view and set. 

    """
    queryset = models.Association.objects.all()
    serializer_class = serializers.AssociationSerializer

class NodeCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows node categories to be view and set
    """
    queryset = models.NodeCategory.objects.all()
    serializer_class = serializers.NodeCategorySerializer

class SettingViewSet(viewsets.ViewSet):
    """
    View to list all settings in rockit server.

    This includes all plugins which got its own settings, the rockit server will just point to it
    using reverse lookup.
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