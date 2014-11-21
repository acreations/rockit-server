from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    return render_to_response('pages/index.html', context_instance=RequestContext(request))

def settings(request):
    return render_to_response('pages/settings/settings.html', context_instance=RequestContext(request))