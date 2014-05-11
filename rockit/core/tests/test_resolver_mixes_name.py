from django.test import TestCase

from rockit.core import resolvers
from rockit.core import models
from rockit.core import holders

class MixesNameResolverTestCase(TestCase):

    def setUp(self):
        self.association = models.Association.objects.create(name = 'my_node', namespace='test')
        self.holder = holders.MixesHolder(self.association)

        models.Node.objects.create(association=self.association, aid=1, name='NODE_1')
        models.Node.objects.create(association=self.association, aid=2, name='NODE_2')
        models.Node.objects.create(association=self.association, aid=3, name='NODE_3')

    def test_it_should_correctly_resolve_names_for_when(self):

        for node in models.Node.objects.all():
            self.holder.add_when(**{
                'identifier': node.aid,
                'name': node.aid
                })

            self.holder.add_then(**{
                'identifier': node.aid,
                'name': node.aid
                })

            self.holder.add_finish(**{
                'identifier': node.aid,
                'name': node.aid
                })

        resolvers.MixesNameResolver().resolve(self.holder)

        for container in self.holder.get_content()['when']:
            for item in container['items']:
                node = models.Node.objects.get(aid=item['identifier'])
                self.assertEqual(node.name, item['name'])

        for container in self.holder.get_content()['then']:
            for item in container['items']:
                node = models.Node.objects.get(aid=item['identifier'])
                self.assertEqual(node.name, item['name'])

        for container in self.holder.get_content()['finish']:
            for item in container['items']:
                node = models.Node.objects.get(aid=item['identifier'])
                self.assertEqual(node.name, item['name'])