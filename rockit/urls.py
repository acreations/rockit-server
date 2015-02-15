import os.path

from django.conf.urls import patterns, include, url

from rockit import settings

from rockit.site import views

urlpatterns = list()

for app in settings.INSTALLED_APPS:
    if app.startswith('rockit'):
        """
        Get all rockit plugins defined in INSTALLED_APPS
        """

        is_plugin = 'plugins' in app

        entry = 'rockit' if not is_plugin else 'rockit/plugins/%s' % app.split('.')[-1]
        ufile = 'rockit.core' if not is_plugin else app

        # If urls.py or urls directory exist then add it otherwise skip it
        if os.path.isfile('%s/urls.py' % entry) or os.path.isdir('%s/urls' % entry):
            urlpatterns += patterns('', url(r'^api/%s/' % entry, include('%s.urls' % ufile)))

        if is_plugin:
            """
            Setup some default urls for plugins
            """
            plugin_entry = app.split('.')[-1]

            urlpatterns += patterns('',
                url(r'partials/%s/settings' % plugin_entry, 'rockit.site.views.settings.partials_settings', { 'entry': plugin_entry })
            )

urlpatterns += patterns('', url('', include('rockit.site.urls')))