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

    def add_when(self, **kwargs):
        """
        Add a when item
        """
        self.append({
            'identifier': kwargs.get('identifier', 'NOT_SET'),
            'association': self.association, 
            'name': kwargs.get('name', 'NOT_SET')
            }, self.CONTAINER_WHEN)

    def _create_container(self, container):
        self.create_group(container)

        return {
            'association': self.association,
            'items': list()
        }