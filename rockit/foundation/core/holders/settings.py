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
        self.append_data(self.generate_setting(key, name, value, readonly))

    def add_setting_group(self, name, settings):
        """
        Add a group of settings

        Keyword arguments:
        name      -- name of group
        settings  -- list of settings

        """
        assert hasattr(settings, "__iter__")

        self.append_data({name: settings})

    def generate_setting(self, key, name, value, readonly=False):
        return {'id': key, 'name':  name, 'value': value, 'isReadonly': readonly}