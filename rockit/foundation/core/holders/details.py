from rockit.foundation.core.holders.holder import Holder

class DetailsHolder(Holder):
    """Details holder is used to help plugins to collect details about a node in network."""

    def add_detail(self, title, value, changeable=False):
        """
        Add a simple detail

        Keyword arguments:
        title -- title
        value -- value

        """
        item = { 
            'title': title,
            'value': value
        }

        if changeable:
            item['url'] = ''

        self.append_data(item)