
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
            for key, instance in instances.items():
                builder = actions.ActionBuilder(instance['commandClasses'])
                builder.filter_actions_by_command_classes(identifier, holder)

        return holder

    def _add_capabilities(self, container, identifier, name):
        container.append({
            'identifier': identifier,
            'name': name
            })

    def _get_then_capabilities(self):
        result = list()

        nodes = models.Node.objects.exclude(device_type__contains='Controller')

        for node in nodes:
            self._add_capabilities(result, node.device_id, node.device_id)

        return result