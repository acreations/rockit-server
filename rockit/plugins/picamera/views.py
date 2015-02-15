from django.shortcuts import render_to_response
from django.template import RequestContext

def partials_settings(request):
    return render_to_response('partials/settings-picamera.html', context_instance=RequestContext(request))