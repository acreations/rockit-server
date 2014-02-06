class SettingsHolder(object):

    def __init__(self):
        self.holder = list()

    def add_simple(self, key, name, value, readonly=False):
        self.holder.append({
            'id':    key,
            'name':  name,
            'value': value,
            'isReadonly': readonly
            })

    def get_content(self):
    	return self.holder