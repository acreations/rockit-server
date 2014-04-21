from rockit.foundation.core.holders.holder import Holder

class WhenHolder(Holder):
    """
    A holder that collects all items that can be assigned to when action
    """
    def __init__(self, association_id):
        super(WhenHolder, self).__init__()

        self.association_id = association_id

    def add(self, identifier, name):
        """
        Add a when item
        """
        self.append({
            'identifier': identifier,
            'association': self.association_id, 
            'name': name
            })