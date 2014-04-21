from rockit.foundation.core import serializers
from rockit.foundation.core.holders.holder import Holder

class WhenHolder(Holder):
    """
    A holder that collects all items that can be assigned to when action
    """
    def __init__(self, association):
        super(WhenHolder, self).__init__()

        self.association = serializers.AssociationSerializer(association).data

    def add(self, identifier, name):
        """
        Add a when item
        """
        self.append({
            'identifier': identifier,
            'association': self.association, 
            'name': name
            })