class Holder(object):
    """A holder object that contains all common functions between two holders"""

    def __init__(self):
        self._content = dict()
        self._content['data'] = list()

    def append_data(self, item):
        """Append something to the holder"""
        self._content['data'].append(item)

    def generate_url_container(self, identifier, args, **kwargs):
        return { 'identifier': identifier }

    def get_content(self):
        """Get contents from holder"""
        return self._content