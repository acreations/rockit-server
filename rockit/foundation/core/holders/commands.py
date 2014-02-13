from rockit.foundation.core.holders.holder import Holder

class CommandsHolder(Holder):
    """Details holder is used to help plugins to collect details about a node in network."""

    def add_switch_command(self, name):
        data = self._generate_base_template(name, 'bool')

        self.append_data(data)

    def add_choice_command(self, name):
        data = self._generate_base_template(name, 'choice')

        self.append_data(data)

    def add_scales_command(self, name):
        data = self._generate_base_template(name, 'scales')

        self.append_data(data)

    def _generate_base_template(self, name, type):
        result = dict()
        result['name'] = name
        result['type'] = type

        return result