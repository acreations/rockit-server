from celery.execute import send_task

from rest_framework import status
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

    def create(self, request):
        """
        Create a new mix
        """

        holder = request.DATA

        validation = holders.ErrorHolder()

        if not self._validate_common(holder, validation):

            validation = self._validate_container('when', holder['when'], validation)
            validation = self._validate_container('then', holder['then'], validation)
            validation = self._validate_container('finish', holder['finish'], validation)

            if not validation.has_errors():

                when = self._create_mix('when', holder['when'], validation)
                then = self._create_mix('then', holder['then'], validation)
                finish = self._create_mix('finish', holder['finish'], validation)

                action = models.Action.objects.create(name=holder['name'], description=holder['description'])

                self._save_mix(action, models.ActionWhen.objects, when)
                self._save_mix(action, models.ActionThen.objects, then)
                self._save_mix(action, models.ActionFinish.objects, finish)

                return Response({'success':False}, status=status.HTTP_404_NOT_FOUND)

        return Response({'success': False , "detail": validation.get_errors() }, status=status.HTTP_400_BAD_REQUEST)

    def _create_mix(self, name, holder, validation):

        result = []

        # Create then action
        for container in holder:
            association = self._get_association(container['entry'], validation)

            if association:
                entry = association.entry

                uuid = self._get_node_uuid(association, container['id'])

                task  = send_task("%s.mixes.%s.create" % (entry, name), args=[uuid, container['criterias']])
                result.append({
                    'id': task.wait(timeout=10),
                    'association': association,
                    'uuid': uuid
                })

        return result

    def _get_association(self, entry, validation):
        try:
            return models.Association.objects.get(entry=entry)
        except models.Association.DoesNotExist:
            validation.add_error(entry, 'Could not find association in network')

        return None

    def _get_node_uuid(self, association, id):
        nodes = models.Node.objects.filter(association=association, aid=id)

        # Should get one and only
        if nodes and len(nodes) is 1:
            return nodes[0].uuid

        # Cannot find node with id, send it back
        return id

    def _save_mix(self, action, model, items):

        for item in items:

            if item['id']:
                created = model.create(holder=action, target=item['association'], identifier=item['id'])

    def _validate_mixes(self, container, holder, validation):

        if 'entry' not in holder or not holder['entry']:
            validation.add_error(container, 'Entry must be provided')

        if 'id' not in holder or not holder['id']:
            validation.add_error(container, 'Node id must be provided')

        if 'criterias' not in holder or not holder['criterias']:
            validation.add_error(container, 'Criterias cannot be empty')

        return validation.has_errors()

    def _validate_criteria(self, container, holder, validation):

        if 'id' not in holder or not holder['id']:
            validation.add_error(container, 'Critieria id must be provided')

        if 'id' not in holder or not holder['id']:
            validation.add_error(container, 'Critieria value must be provided')

        return validation.has_errors()

    def _validate_container(self, name, holder, validation):

        # Validate when criterias
        for container in holder:

            if not self._validate_mixes(name, container, validation):

                for key, criteria in container['criterias'].iteritems():
                    self._validate_criteria(container['id'], criteria, validation)

                if not validation.has_errors():

                    association = self._get_association(container['entry'], validation)

                    if association:
                        entry = association.entry
                        task  = send_task("%s.mixes.%s.validate" % (entry,name), args=[container['id'], container['criterias'], validation])

                        # Wait for return validation holder
                        return task.wait(timeout=10)

        return validation

    def _validate_common(self, holder, validation):

        # Make sure that name is
        if 'name' not in holder or not holder['name']:
            validation.add_error('name', 'Name cannot be empty')

        if 'when' not in holder:
            validation.add_error('when', 'When container must be provided')

        if 'then' not in holder or not holder['then']:
            validation.add_error('then', 'Then container must be provided')

        if 'finish' not in holder:
            validation.add_error('finish', 'When container must be provided')

        return validation.has_errors()