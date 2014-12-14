from django.conf.urls import patterns, include, url

from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = patterns('',
    url('', include(router.urls))
)