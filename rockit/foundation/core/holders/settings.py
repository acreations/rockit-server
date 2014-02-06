from rockit.foundation.core.holders.holder import Holder

class SettingsHolder(Holder):

    def add_simple(self, key, name, value, readonly=False):
        self.append({
            'id':    key,
            'name':  name,
            'value': value,
            'isReadonly': readonly
            })