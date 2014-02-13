from rockit.foundation.core.holders.holder import Holder

class DetailsHolder(Holder):
    """Details holder is used to help plugins to collect details about a node in network."""

    def add_detail(self, title, value):
        """
        Add a simple detail

        Keyword arguments:
        title -- title
        value -- value

        """
        self.append({
            'title': title,
            'value': value
            })
