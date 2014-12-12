from django.conf import settings
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'rockit.site.views.home', name='home'),
    url(r'^nodes/', 'rockit.site.views.node', name='node'),
    url(r'^nodes', 'rockit.site.views.nodes', name='nodes'),
    url(r'^settings', 'rockit.site.views.settings', name='settings'),
)
