
class Holder(object):

    def __init__(self):
        self._content = list()

    def append(self, item):
        self._content.append(item)

    def get_content(self):
        return self._content