from django.conf import settings
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
		url(r'^$', 'rockit.site.views.home', name='home'),
		url(r'^settings$', 'rockit.site.views.settings', name='settings'),
)
