import os.path

from django.conf.urls import patterns, include, url

from rockit import settings

urlpatterns = list()

for app in settings.INSTALLED_APPS:
    if app.startswith('rockit'):
        '''
        Get all rockit plugins defined in INSTALLED_APPS
        '''
        entry = 'rockit' if 'plugins' not in app else 'rockit/plugins/%s' % app.split('.')[-1]
        ufile = 'rockit.core' if 'plugins' not in app else app

        # If urls.py or urls directory exist then add it otherwise skip it
        if os.path.isfile('%s/urls.py' % entry) or os.path.isdir('%s/urls' % entry):
          urlpatterns += patterns('', url(r'^api/%s/' % entry, include('%s.urls' % ufile)))

urlpatterns += patterns('', url('', include('rockit.site.urls')))