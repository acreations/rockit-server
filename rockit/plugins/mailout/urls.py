from django.conf.urls import patterns, include, url

from rest_framework import routers

from rockit.foundation.core import views

router = routers.DefaultRouter()
router.register('nodes',  views.NodeViewSet, base_name='mailout-addable')

urlpatterns = patterns('',
    url('', include(router.urls))
)