from rockit.core import serializers
from rockit.core.holders import Holder

class MixesHolder(Holder):
    """
    A holder that collects all items that can be assigned to when action
    """

    CONTAINER_WHEN = 'when'
    CONTAINER_THEN = 'then'
    CONTAINER_FINAL = 'final'

    def __init__(self, association):
        super(MixesHolder, self).__init__()

        self.association = serializers.AssociationSerializer(association).data

        self.when = self._create_container(self.CONTAINER_WHEN)
        self.then = self._create_container(self.CONTAINER_THEN)
        self.final = self._create_container(self.CONTAINER_FINAL)

        self.dirty = False

    def add_when(self, **kwargs):
        """
        Add a when item
        """
        self.when['items'].append({
            'identifier': kwargs.get('identifier', 'NOT_SET'),
            'name': kwargs.get('name', 'NOT_SET')
        })

        self.dirty = True

    def get_content(self):
        """
        Override by adding when, then, final before get content
        """
        if self.dirty:
            self.reset_group(self.CONTAINER_WHEN)
            self.reset_group(self.CONTAINER_THEN)
            self.reset_group(self.CONTAINER_FINAL)

            self.append(self.when, self.CONTAINER_WHEN)
            self.append(self.then, self.CONTAINER_THEN)
            self.append(self.final, self.CONTAINER_FINAL)
        
        return super(MixesHolder, self).get_content()

    def _create_container(self, container):
        self.create_group(container)

        return {
            'association': self.association,
            'items': list()
        }