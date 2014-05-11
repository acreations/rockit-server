from rockit.core import serializers
from rockit.core.holders import Holder

class MixesHolder(Holder):
    """
    A holder that collects all items that can be assigned to when action
    """

    CONTAINER_WHEN = 'when'
    CONTAINER_THEN = 'then'
    CONTAINER_FINISH = 'finish'

    def __init__(self, association):
        super(MixesHolder, self).__init__()

        self.association = serializers.AssociationSerializer(association).data

        self.when = self._create_container(self.CONTAINER_WHEN)
        self.then = self._create_container(self.CONTAINER_THEN)
        self.finish = self._create_container(self.CONTAINER_FINISH)

        self.dirty = False

        self.resolve_names = False;

    def add_finish(self, **kwargs):
        """
        Add a final item
        """
        self._add(self.finish, **kwargs)

    def add_then(self, **kwargs):
        """
        Add a then item
        """
        self._add(self.then, **kwargs)

    def add_when(self, **kwargs):
        """
        Add a when item
        """
        self._add(self.when, **kwargs)

    def get_content(self):
        """
        Override by adding when, then, final before get content
        """
        if self.dirty:
            self.reset_group(self.CONTAINER_WHEN)
            self.reset_group(self.CONTAINER_THEN)
            self.reset_group(self.CONTAINER_FINISH)

            if len(self.when['items']) > 0:
                self.append(self.when, self.CONTAINER_WHEN)

            if len(self.then['items']) > 0:
                self.append(self.then, self.CONTAINER_THEN)

            if len(self.finish['items']) > 0:
                self.append(self.finish, self.CONTAINER_FINISH)
        
        return super(MixesHolder, self).get_content()

    def mark_resolve_names(self):
        self.resolve_names = True;

    def should_resolve_names(self):
        return self.resolve_names;

    def _add(self, container, **kwargs):

        container['items'].append({
            'identifier': kwargs.get('identifier', 'NOT_SET'),
            'name': kwargs.get('name', 'NOT_SET')
        })

        self.dirty = True

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
    def __init__(self):
        super(MixesDetailsHolder, self).__init__()

        self.container = dict()
        self.dirty = False

        self.name = 'POST'

    def add_post(self, **kwargs):
        """
        Add post update data
        """
        self._create_data('POST', **kwargs)
        
    def add_update(self, **kwargs):
        self._create_data('PUT', **kwargs)

    def get_content(self):
        """
        Override by post before calling super class
        """
        if self.dirty:
            self.reset_group('actions')

            self.append({ '%s' % self.name : self.container }, 'actions', True)

        if len(self.container) is 0:
            self.reset_group('actions')

        return super(MixesDetailsHolder, self).get_content()

    def _create_data(self, name, **kwargs):
        self.name = name

        data = {
            'type': kwargs.get('type', ''),
            'required': kwargs.get('required', False),
            'label': kwargs.get('label', ''),
        }

        if 'max_length' in kwargs:
            data['max_length'] = kwargs.get('max_length', 0)

        self.container[kwargs.get('identifier', 'UNKNOWN_IDENTIFIER')] = data
        self.dirty = True
