from django.conf.urls import patterns, include, url

# Include all urls in rockit foundation
urlpatterns = patterns('',
    url('', include('rockit.foundation.core.urls'))
)