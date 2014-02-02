#from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()

#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rockit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
#)

from django.conf.urls import patterns, include, url

from rockit.foundation.core import models

urlpatterns = list()

for assoc in models.Association.objects.all():
	try:
		urlpatterns += patterns('', url(r'%s/' % assoc.entry, include(assoc.namespace + '.urls')))
	except ImportError:
		continue