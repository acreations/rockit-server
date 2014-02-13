from rockit.foundation.core.holders.holder import Holder

class SettingsHolder(Holder):
	"""Settings holder is used to help plugins to collect settings."""

    def add_setting(self, key, name, value, readonly=False):
    	"""
    	Add a simple settings

    	Keyword arguments:
    	key      -- unique key
    	name     -- name 
    	value    -- current value
    	readonly -- specifies if this is readonly

    	"""
        self.append({'id': key, 'name':  name, 'value': value, 'isReadonly': readonly})