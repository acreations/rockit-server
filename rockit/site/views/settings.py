import os.path

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

def partials_settings(request, entry):

    partials = 'partials/settings-%s.html' % entry

    if not os.path.isfile('%s/rockit/plugins/%s/templates/%s' % (settings.BASE_DIR, entry, partials)):
        """
        Use default if not finding templates
        """
        partials = 'partials/settings/settings-default.html'

    return render_to_response(partials, context_instance=RequestContext(request))