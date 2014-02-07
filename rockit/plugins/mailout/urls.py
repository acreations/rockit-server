from django.conf.urls import patterns, include, url

from rest_framework import routers

from rockit.plugins.mailout import views

router = routers.DefaultRouter()
router.register('nodes',   views.NodeViewSet)
router.register('servers', views.ServerViewSet)

urlpatterns = patterns('abc',
    url('', include(router.urls))
)