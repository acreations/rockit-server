
class Holder(object):
    """
    A holder is used to encapsulate messages between Rockit and its plugins.
    It creates a standard way of communication.

    This object contains common functionality for all holders.
    """

    def __init__(self):
        self._content = dict()

    def append(self, item, group='items', override=False):
        """
        Append arbitary item to holder

        If item is a type list then extend will be used instead of append
        """
        if override:
            self._content[group] = item
        else:
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

    def create_group(self, group):
        """
        Create a new group in content dict
        """
        if group not in self._content:
            self.reset_group(group)

    def extend(self, holder):
        """
        Extend current holder with another one
        """
        for key in holder.get_content():
            self.append(holder.get_content()[key], key)

    def get_content(self):
        """
        Get contents from holder
        """
        return self._content

    def reset(self):
        """
        Clear contents from this holder
        """
        self._content = dict()

    def reset_group(self, group):
        """
        Reset specific group
        """
        if group:
            self._content[group] = list()
