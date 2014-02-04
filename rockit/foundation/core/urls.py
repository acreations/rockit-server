from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from rest_framework import routers

from rockit.foundation.core import models
from rockit.foundation.core import views

router = routers.DefaultRouter()
router.register('association',  views.AssociationViewSet)
router.register('settings-all', views.AllSettingsViewSet, base_name="rockit-settings-all")

urlpatterns = patterns('',
	url('', include(router.urls)),
	url(r'^settings', views.SettingViewSet.as_view({'get': 'list'}), name='rockit-settings')
)