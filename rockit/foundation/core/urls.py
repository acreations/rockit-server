from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from rest_framework import routers

from rockit.foundation.core import models
from rockit.foundation.core import views

router = routers.DefaultRouter()
router.register('associations',  views.AssociationViewSet)
router.register('settings', views.SettingViewSet, base_name="setting")

urlpatterns = patterns('',
	url('', include(router.urls))
)