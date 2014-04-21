class Holder(object):
    """
    A holder is used to encapsulate messages between Rockit and its plugins. It creates a standard way of communication.

    This object contains common functionality for all holders.
    """
    def __init__(self):
        self._content = dict()
        self._content['data'] = list()

    def append(self, item):
        """
        Append arbitary item to holder

        If item is a type list then extend will be used instead of append
        """
        if type(item) is list:
            self._content['data'].extend(item)
        else:
            self._content['data'].append(item)

    def extend(self, holder):
        """
        Extend current holder with another one
        """
        self.append(holder.get_content()['data'])

    def append_data(self, item):
        """Append data to the holder"""
        self._content['data'].append(item)

    def generate_url_container(self, identifier, args, **kwargs):
        """Generate url container"""
        return { 
            'identifier': identifier 
        }

    def get_content(self):
        """Get contents from holder"""
        return self._content