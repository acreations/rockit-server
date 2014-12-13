from django.conf import settings
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'rockit.site.views.home', name='home'),
    url(r'^nodes/', 'rockit.site.views.node', name='node'),
    url(r'^settings', 'rockit.site.views.settings', name="settings"),
    url(r'^partials/home', 'rockit.site.views.part_home'),
    url(r'^partials/nodes', 'rockit.site.views.part_nodes'),
)
