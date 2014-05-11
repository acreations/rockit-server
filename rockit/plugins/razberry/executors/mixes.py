
from rockit.plugins.razberry import models

class MixesExecutor(object): 

    def collect(self, holder):
        """
        Collect capabilities of this executor
        """
        
        for c in self._get_when_capabilities():
            holder.add_when(**c)

        return holder

    def _add_capabilities(self, container, identifier, name):
        container.append({
            'identifier': identifier,
            'name': name
            })

    def _get_then_capabilities(self):
        result = list()

        nodes = models.Nodes.object.exclude(device_type__contains='Controller').get()

        for node in nodes:
            result.push(_add_capabilities(result, node.device_id, node.device_id))

        return result