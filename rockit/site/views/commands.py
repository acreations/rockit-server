from django.shortcuts import render_to_response
from django.template import RequestContext

def command_switch_binary(request):
    return render_to_response('partials/commands/SwitchBinary.html', context_instance=RequestContext(request))
