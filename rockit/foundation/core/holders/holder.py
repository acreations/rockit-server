class Holder(object):
    """A holder object that contains all common functions between two holders"""

    def __init__(self):
        self._content = list()

    def append(self, item):
        """Append something to the holder"""
        self._content.append(item)

    def get_content(self):
        """Get contents from holder"""
        return self._content