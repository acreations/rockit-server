from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from rest_framework import routers

from rockit.core import models
from rockit.core import views

router = routers.DefaultRouter()
router.register('mixes',  views.MixesViewSet, base_name="mixes")
router.register('actions',  views.ActionViewSet)
router.register('associations',  views.AssociationViewSet)
router.register('categories',  views.NodeCategoryViewSet)
router.register('nodes',  views.NodeViewSet)
router.register('settings', views.SettingViewSet, base_name="setting")
router.register('schedules', views.ScheduleViewSet)

urlpatterns = patterns('',
    url('', include(router.urls)),
    url('^nodes/(?P<pk>\d+)/commands/(?P<cid>[\d\w.]+)/value/(?P<value>[\d\w]+)', views.CommandUpdateViewSet.as_view(), name="commands-set"),
    url('^nodes/(?P<pk>\d+)/commands/(?P<cid>[\d\w.]+)', views.CommandRetrieveViewSet.as_view(), name="commands-get"),
    url('^mixes/(?P<pk>[a-zA-Z0-9\-]+)/(?P<wtf>[a-zA-Z]+)/(?P<entry>[a-zA-Z]+)/$', views.MixesViewSet.as_view({'get': 'details'}), name="mixes-details")
)