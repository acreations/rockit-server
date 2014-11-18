from django.conf import settings
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'rockit.site.views.index', name='home'),
)
