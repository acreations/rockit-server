from rockit.core.holders import Holder

class DetailsHolder(Holder):
    """
    Details holder is used to help plugins to collect details about a node in network.
    """

    def add(self, **kwargs):
        """
        Add a simple detail

        Keyword arguments:
        title -- title
        value -- value

        """
        item = { 
            'title': kwargs.get('title', 'NOT_SET'),
            'value': kwargs.get('value', 'NOT_SET')
        }

        if 'url' in kwargs:
            result['url'] = kwargs.get('url', 'BAD_URL')

        self.append(item)