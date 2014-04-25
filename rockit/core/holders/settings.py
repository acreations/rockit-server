from rockit.core.holders import Holder

class SettingsHolder(Holder):
    """
    Settings holder is used to help plugins to collect settings.

    Supported kwargs:

    {
        key:   unique key (when updating)
        name:  name 
        value: value
        readonly: readonly?
    }
    """

    def add(self, **kwargs):
        """
        Add a simple settings
        """
        self.append(self.normalize(**kwargs))

    def add_to_group(self, name, settings):
        """
        Add a group of settings

        Keyword arguments:
        name      -- name of group
        settings  -- list of settings

        """
        assert hasattr(settings, "__iter__")

        self.append({
            'name': name,
            'settings': settings
            })

    def normalize(self, **kwargs):
        """
        Normalize as a setting type
        """
        result = {
            'id': kwargs.get('key', 'NOT_SET'),
            'name': kwargs.get('name', 'NOT_SET'),
            'value': kwargs.get('value', 'NOT_SET'),
            'readonly': kwargs.get('readonly', True)
            }

        if 'url' in kwargs:
            result['url'] = kwargs.get('url', 'BAD_URL')

        return result