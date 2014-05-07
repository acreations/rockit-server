
class MixesExecutor(object): 

    IDENTIFIER_BUTTON   = 'when-button'
    IDENTIFIER_SCHEDULE = 'when-schedule'

    IDENTIFIER_MAILOUT  = 'finish-mailout' 

    def __init__(self):
        self.details = {
            self.IDENTIFIER_BUTTON: lambda h: self._set_when_button_details(h)
        }

    def collect(self, holder):
        """
        Collect capabilities of this executor
        """
        for c in self._get_when_capabilities():
            holder.add_when(**c)

        return holder

    def collect_details(self, identifier, holder):
        """
        Collect details about specific mixes
        """
        assert identifier is not None
        assert holder is not None

        if identifier in self.details:
            self.details[identifier](holder)

        return holder

    def _add_capabilities(self, container, identifier, name):
        container.append({
            'identifier': identifier,
            'name': name
            })

    def _generate_post(self, identifier, typed, label, required=False, max_length=None):
        
        data = {
            'identifier': identifier,
            'type': typed,
            'label': label,
            'required': required
        }

        if max_length:
            data['max_length'] = max_length

        return data

    def _get_when_capabilities(self):
        result = list()

        self._add_capabilities(result, self.IDENTIFIER_BUTTON, 'button')
        self._add_capabilities(result, self.IDENTIFIER_SCHEDULE, 'schedule')

        return result

    def _get_finish_capabilities(self):
        result = list()

        self._add_capabilities(result, self.IDENTIFIER_MAILOUT, 'mailout')

        return result

    def _set_when_button_details(self, holder):
        holder.add_post(**self._generate_post('name', 'string', 'name', True, 100))
