
class MixesExecutor(object): 

    IDENTIFIER_BUTTON   = 'when-button';
    IDENTIFIER_SCHEDULE = 'when-schedule';

    def collect(self, holder):
        '''
        Collect capabilities of this executor
        '''
        for c in self._get_when_capabilities():
            holder.add_when(**c)

        return holder

    def _add_when_capabilities(self, container, identifier, name):
        container.append({
            'identifier': identifier,
            'name': name
            })

    def _get_when_capabilities(self):
        result = list()

        self._add_when_capabilities(result, self.IDENTIFIER_BUTTON, 'button')
        self._add_when_capabilities(result, self.IDENTIFIER_SCHEDULE, 'schedule')

        return result