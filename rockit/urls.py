from django.conf.urls import patterns, include, url

from rockit.foundation.core import models

urlpatterns = list()

for a in models.Association.objects.all():
    try:
        prefix = ''

        if('plugins' in a.namespace):
            prefix = 'plugins/'

        urlpatterns += patterns('', url(r'^%s%s/' % (prefix,a.entry), include(a.namespace + '.urls')))
    except ImportError:
        continue