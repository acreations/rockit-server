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
        
        urlpatterns += patterns('', url(r'^%s/' % entry, include('%s.urls' % ufile)))