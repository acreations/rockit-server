class Holder(object):
    """
    A holder is used to encapsulate messages between Rockit and its plugins. It creates a standard way of communication.

    This object contains common functionality for all holders.
    """

    def __init__(self):
        self._content = dict()

    def create_group(self, group):
        '''
        Create a new group in content dict
        '''
        if group not in self._content:
            self._content[group] = list()

    def append(self, item, group='items'):
        """
        Append arbitary item to holder

        If item is a type list then extend will be used instead of append
        """

        self.create_group(group)

        if type(item) is list:
            self._content[group].extend(item)
        else:
            self._content[group].append(item)

    def consume(self):
        """
        Consume contents from holder (read it and reset holder afterwards)
        """
        result = self.get_content()

        self.reset()

        return result

    def extend(self, holder):
        """
        Extend current holder with another one
        """
        for key in holder.get_content()['data']:
            self.append(holder.get_content()['data'][key], key)

    def get_content(self):
        """
        Get contents from holder
        """
        return {
            'data': self._content
        }

    def reset(self):
        """
        Clear contents from this holder
        """
        self._content = dict()