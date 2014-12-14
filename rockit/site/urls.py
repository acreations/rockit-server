from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'rockit.site.views.home', name='home'),
    url(r'^partials/home', 'rockit.site.views.part_home'),
    url(r'^partials/commands/SwitchBinary', 'rockit.site.views.command_switch_binary'),
    url(r'^partials/nodes/details/razberry', 'rockit.site.views.part_nodes_details_razberry'),
    url(r'^partials/nodes/details', 'rockit.site.views.part_nodes_details'),
    url(r'^partials/nodes', 'rockit.site.views.part_nodes'),
    url(r'^partials/mixes', 'rockit.site.views.part_mixes'),
    url(r'^partials/settings', 'rockit.site.views.part_settings'),
)
