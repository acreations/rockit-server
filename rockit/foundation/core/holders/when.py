from rockit.foundation.core.holders.holder import Holder

class WhenHolder(Holder):
    """
    A holder that collects all items that can be assigned to when action
    """

    def add(self, identifier, name):
        """
        Add a when item
        """
        self.append({
            'identifier': identifier,
            'name': name
            })