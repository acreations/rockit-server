from django.conf.urls import patterns, include, url

from rockit.foundation.core import models
from rockit import settings

urlpatterns = list()

for a in models.Association.objects.all():
    try:
        prefix = ''

        if('plugins' in a.namespace):
            prefix = 'plugins/'

        urlpatterns += patterns('', url(r'^%s%s/' % (prefix,a.entry), include(a.namespace + '.urls')))
    except ImportError:
        continue

#for app in settings.INSTALLED_APPS:
#    if app.startswith('rockit'):
#        entry = 'rockit' if 'plugins' not in app else app.split('.')[-1]
#        urls  = '%s.urls' % app
#        urlpatterns += patterns('', url(r'^%s/' % entry, include(app)))
