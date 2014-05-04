
class MixesExecutor(object): 

    IDENTIFIER_BUTTON   = 1001;
    IDENTIFIER_SCHEDULE = 1002;

    when_capabilities = []

    def __init__(self):

        self._add_when_capabilities(self.IDENTIFIER_BUTTON, 'button')
        self._add_when_capabilities(self.IDENTIFIER_SCHEDULE, 'schedule')

    def collect(self, holder):
        '''
        Collect capabilities of this executor
        '''
        holder.reset()

        for c in self.when_capabilities:
            holder.add_when(**c)

        return holder

    def _add_when_capabilities(self, identifier, name):
        self.when_capabilities.append({
            'identifier': identifier,
            'name': name
            })