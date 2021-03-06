
from rockit.plugins.razberry import models
from rockit.plugins.razberry import services

class MixesExecutor(object):

    def __init__(self):

        self.supported = {
            '37': lambda c: self._get_switch_binary_data(c),
        }

    def collect(self, holder):
        """
        Collect capabilities of this executor
        """

        for c in self._get_then_capabilities():
            holder.mark_resolve_names()
            holder.add_then(**c)

        return holder

    def collect_details(self, identifier, holder):
        """
        Collect details
        """
        instances = services.RazberryService().retrieve_instances(identifier)

        if instances:

            for key, instance in instances.items():
                self._append_command_details(identifier, holder, instance['commandClasses'])

        return holder

    def validate(self, criterias, validation):

        for key, criteria in criterias.iteritems():
            instance = services.RazberryService().retrieve(criteria['id'])

            if instance:
                identifier = str(instance['id'])

                if identifier in self.supported:
                    data = self.supported[identifier](instance)

                    if data['required'] and not criteria['value']:
                        validation.add_error(criteria['id'], 'Criteria value cannot be empty')

        return validation

    def _add_capabilities(self, container, identifier, name):
        container.append({
            'identifier': identifier,
            'name': name
            })

    def _append_command_details(self, identifier, holder, commandClasses):

        for key in commandClasses:
            command = commandClasses[key]

            if command['supported'] and key in self.supported:
                holder.add_post(**self.supported[key](command))

    def _get_switch_binary_data(self, command):
        return {
            'identifier': command['data']['name'].replace('.data',''),
            'type': 'select',
            'required': True,
            'label': command['name'],
            'value': ['$toggle',True,False]
        }

    def _get_then_capabilities(self):
        result = list()

        nodes = models.Node.objects.exclude(device_type__contains='Controller')

        for node in nodes:
            self._add_capabilities(result, node.device_id, node.device_id)

        return result
