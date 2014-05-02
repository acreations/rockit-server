
class WhenExecutor(object): 

    IDENTIFIER_BUTTON   = 1001;
    IDENTIFIER_SCHEDULE = 1002;

    capabilities = []

    def __init__(self):

        self._add_capabilities(self.IDENTIFIER_BUTTON, 'button')
        self._add_capabilities(self.IDENTIFIER_SCHEDULE, 'schedule')

    def collect(self, holder):
        '''
        Collect capabilities of this executor
        '''
        for c in self.capabilities:
            holder.add(**c)

        return holder

    def _add_capabilities(self, identifier, name):
        self.capabilities.append({
            'identifier': identifier,
            'name': name
            })