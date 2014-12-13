from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    return render_to_response('pages/index.html', context_instance=RequestContext(request))

def nodes(request):
    return render_to_response('pages/nodes/nodes.html', context_instance=RequestContext(request))

def node(request):
    return render_to_response('pages/nodes/details.html', context_instance=RequestContext(request))

def settings(request, setting=""):
    return render_to_response('pages/settings/settings.html', context_instance=RequestContext(request))