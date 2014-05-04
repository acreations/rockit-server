from rockit.core import serializers
from rockit.core.holders import Holder

class MixesHolder(Holder):
    """
    A holder that collects all items that can be assigned to when action
    """

    CONTAINER_WHEN = 'when'
    CONTAINER_THEN = 'then'
    CONTAINER_FINALLY = 'finally'

    def __init__(self, association):
        super(MixesHolder, self).__init__()

        self.association = serializers.AssociationSerializer(association).data

        self.create_group(self.CONTAINER_WHEN)
        self.create_group(self.CONTAINER_THEN)
        self.create_group(self.CONTAINER_FINALLY)

    def add_when(self, **kwargs):
        """
        Add a when item
        """
        self.append({
            'identifier': kwargs.get('identifier', 'NOT_SET'),
            'association': self.association, 
            'name': kwargs.get('name', 'NOT_SET')
            }, self.CONTAINER_WHEN)