from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    return render_to_response('pages/index.html', context_instance=RequestContext(request))

def part_home(request):
    return render_to_response('partials/home.html', context_instance=RequestContext(request))

def part_mixes(request):
    return render_to_response('partials/mixes/mixes.html', context_instance=RequestContext(request))

def part_nodes(request):
    return render_to_response('partials/nodes/nodes.html', context_instance=RequestContext(request))

def part_nodes_details(request):
    return render_to_response('partials/nodes/details.html', context_instance=RequestContext(request))

def part_nodes_details_razberry(request):
    return render_to_response('partials/nodes/details-razberry.html', context_instance=RequestContext(request))

def part_settings(request, setting=""):
    return render_to_response('partials/settings/settings.html', context_instance=RequestContext(request))
