
from rockit.plugins.razberry import models
from rockit.plugins.razberry import services

class MixesExecutor(object): 

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
            self.supported = {
                '37': lambda h, c: self._generalize_switch_binary(h, c),
            }

            for key, instance in instances.items():
                self._append_command_details(identifier, holder, instance['commandClasses'])

        return holder

    def _add_capabilities(self, container, identifier, name):
        container.append({
            'identifier': identifier,
            'name': name
            })
    
    def _append_command_details(self, identifier, holder, commandClasses):

        for key in commandClasses:
            command = commandClasses[key]

            if command['supported'] and key in self.supported:
                self.supported[key](holder, command)

    def _generalize_switch_binary(self, holder, command):
        holder.add_post(**{
            'type': 'radio',
            'required': True,
            'label': command['name'],
            'value': ''
            })

    def _get_then_capabilities(self):
        result = list()

        nodes = models.Node.objects.exclude(device_type__contains='Controller')

        for node in nodes:
            self._add_capabilities(result, node.device_id, node.device_id)

        return result
