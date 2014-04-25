from rockit.core import serializers
from rockit.core.holders import Holder

class WhenHolder(Holder):
    """
    A holder that collects all items that can be assigned to when action
    """
    def __init__(self, association):
        super(WhenHolder, self).__init__()

        self.association = serializers.AssociationSerializer(association).data

    def add(self, **kwargs):
        """
        Add a when item
        """
        self.append({
            'identifier': kwargs.get('identifier', 'NOT_SET'),
            'association': self.association, 
            'name': kwargs.get('name', 'NOT_SET')
            })