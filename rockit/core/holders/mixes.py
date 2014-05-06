from rockit.core import serializers
from rockit.core.holders import Holder

class MixesHolder(Holder):
    """
    A holder that collects all items that can be assigned to when action
    """

    CONTAINER_WHEN = 'when'
    CONTAINER_THEN = 'then'
    CONTAINER_FINAL = 'final'

    def __init__(self, association):
        super(MixesHolder, self).__init__()

        self.association = serializers.AssociationSerializer(association).data

        self.when = self._create_container(self.CONTAINER_WHEN)
        self.then = self._create_container(self.CONTAINER_THEN)
        self.final = self._create_container(self.CONTAINER_FINAL)

        self.dirty = False

    def add_final(self, **kwargs):
        """
        Add a final item
        """
        self.final['items'].append({
            'identifier': kwargs.get('identifier', 'NOT_SET'),
            'name': kwargs.get('name', 'NOT_SET')
        })

        self.dirty = True


    def add_then(self, **kwargs):
        """
        Add a then item
        """
        self.then['items'].append({
            'identifier': kwargs.get('identifier', 'NOT_SET'),
            'name': kwargs.get('name', 'NOT_SET')
        })

        self.dirty = True

    def add_when(self, **kwargs):
        """
        Add a when item
        """
        self.when['items'].append({
            'identifier': kwargs.get('identifier', 'NOT_SET'),
            'name': kwargs.get('name', 'NOT_SET')
        })

        self.dirty = True


    def get_content(self):
        """
        Override by adding when, then, final before get content
        """
        if self.dirty:
            self.reset_group(self.CONTAINER_WHEN)
            self.reset_group(self.CONTAINER_THEN)
            self.reset_group(self.CONTAINER_FINAL)

            if len(self.when['items']) > 0:
                self.append(self.when, self.CONTAINER_WHEN)

            if len(self.then['items']) > 0:
                self.append(self.then, self.CONTAINER_THEN)

            if len(self.final['items']) > 0:
                self.append(self.final, self.CONTAINER_FINAL)
        
        return super(MixesHolder, self).get_content()

    def _create_container(self, container):
        self.create_group(container)

        return {
            'association': self.association,
            'items': list()
        }

class MixesDetailsHolder(Holder):
    """
    Mixes details holder
    """
    CONTAINER_POST = 'POST'
    CONTAINER_ACTION = 'actions'

    def __init__(self):
        super(MixesDetailsHolder, self).__init__()

        self.post = dict()
        self.dirty = False

    def add_post(self, **kwargs):
        """
        Add post update data
        """
        data = {
            'type': kwargs.get('type', 'NOT_SET'),
            'required': kwargs.get('required', False),
            'label': kwargs.get('label', 'NOT_SET'),
        }

        if 'max_length' in kwargs:
            data['max_length'] = kwargs.get('max_length', 0)

        self.post[kwargs.get('identifier', 'UNKNOWN_IDENTIFIER')] = data
        self.dirty = True

    def get_content(self):
        """
        Override by post before calling super class
        """
        if self.dirty:
            self.reset_group(self.CONTAINER_ACTION)

            if len(self.post):
                self.append({ '%s' % self.CONTAINER_POST : self.post }, self.CONTAINER_ACTION, True)

        if len(self.post) is 0:
            self.reset_group(self.CONTAINER_ACTION)

        return super(MixesDetailsHolder, self).get_content()
