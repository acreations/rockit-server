from rockit.core.holders import Holder

class CommandsHolder(Holder):
    """
    The command holder holds all commands set by a given plugin.
    """

    def add_switch_command(self, identifier, name, on_value, off_value, current_value):
        """Add a binary switch command data"""
        data = self._generate_base_template(identifier, name, 'binary')

        data['values']['on']  = on_value
        data['values']['off'] = off_value
        data['values']['current'] = current_value

        self.append_data(data)

    def add_choice_command(self, name):
        """Add a choice command data"""
        data = self._generate_base_template(name, 'choice')

        self.append_data(data)

    def add_scales_command(self, name):
        """Add scales command data"""
        data = self._generate_base_template(name, 'scales')

        self.append_data(data)

    def _generate_base_template(self, identifier, name, typed):
        result = dict()
        result['id']   = identifier
        result['name'] = name
        result['type'] = typed
        result['values'] = dict()

        return result