from django.shortcuts import render_to_response
from django.template import RequestContext

def partials_settings(request, entry):
    print entry

    return render_to_response('partials/settings-alarm.html', context_instance=RequestContext(request))