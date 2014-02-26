from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from rest_framework import routers

from rockit.foundation.core import models
from rockit.foundation.core import views

router = routers.DefaultRouter()
router.register('addables',  views.AddableViewSet, base_name="addable")
router.register('actions',  views.ActionViewSet)
router.register('associations',  views.AssociationViewSet)
router.register('categories',  views.NodeCategoryViewSet)
router.register('nodes',  views.NodeViewSet)
router.register('settings', views.SettingViewSet, base_name="setting")

urlpatterns = patterns('',
    url('', include(router.urls)),
    url('^nodes/(?P<pk>\d+)/commands/(?P<cid>\d+)/value/(?P<value>\d+)', views.CommandUpdateViewSet.as_view(), name="commands-set"),
    url('^nodes/(?P<pk>\d+)/commands/(?P<cid>\d+)', views.CommandRetrieveViewSet.as_view(), name="commands-get")
)