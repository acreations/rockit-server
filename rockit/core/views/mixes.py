from celery.execute import send_task

from django.db import transaction

from rest_framework import viewsets
from rest_framework.response import Response

from rockit.core import models
from rockit.core import holders
from rockit.core import resolvers
from rockit.core import serializers

class MixesViewSet(viewsets.ViewSet):
    """
    List all addable mix states in rockit server
    """

    def list(self, request):
        """
        Return a list of all addables.
        """
        result = holders.Holder()

        for a in models.Association.objects.all():
            task = send_task("%s.mixes" % a.entry, args=[holders.MixesHolder(a)])
            mixes = task.wait(timeout=10)

            if mixes:
                mixes = resolvers.MixesResolver().resolve(request, mixes)
                result.extend(resolvers.MixesNameResolver().resolve(mixes) if mixes.should_resolve_names() else mixes)

        return Response(result.get_content())

    def details(self, request, *args, **kwargs):
        """
        Return specifc options for the requested mix
        """

        entry = kwargs['entry']
        identifier = kwargs['pk']

        task = send_task("%s.mixes.details" % entry, args=[identifier, holders.MixesDetailsHolder()])
        mixes = task.wait(timeout=10)

        return Response(mixes.get_content())

    @transaction.commit_on_success
    def create(self, request):
        """
        Create a new mix
        """

        holder = request.DATA

        action = models.Action.objects.create(name=holder['name'], description=holder['description'])

        for criteria in holder['then']:
            node = models.Node.objects.get(pk=criteria['id'])

            for command in criteria['values']:
                models.ActionThen.objects.create(holder=action, target=node, command=command['id'], value=command['value'])

        return Response({'success':True})