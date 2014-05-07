from django.test import TestCase

from rockit.core import holders
from rockit.core import models

class MixesHolderTestCase(TestCase):

    def setUp(self):
        self.association = models.Association.objects.create(name = 'my_node', namespace='test')

        self.holder = holders.MixesHolder(self.association)

    def test_it_should_contain_when_then_finally(self):
        content = self.holder.get_content()
        self.assertNotEqual(None, content['when'])
        self.assertNotEqual(None, content['then'])
        self.assertNotEqual(None, content['finish'])

    def test_it_should_not_containing_any_values(self):
        content = self.holder.get_content()
        self.assertEqual(0, len(content['when']))
        self.assertEqual(0, len(content['then']))
        self.assertEqual(0, len(content['finish']))

    def test_it_should_be_able_to_add_final(self):
        self.holder.add_finish(**{
            'identifier': 1,
            'name': 'MY_NAME'
            })

        content = self.holder.get_content()['finish']

        self.assertEqual(True, 'MY_NAME' in str(content))

    def test_it_should_be_able_to_add_then(self):
        self.holder.add_then(**{
            'identifier': 1,
            'name': 'MY_NAME'
            })

        content = self.holder.get_content()['then']

        self.assertEqual(True, 'MY_NAME' in str(content))

    def test_it_should_be_able_to_add_when(self):
        self.holder.add_when(**{
            'identifier': 1,
            'name': 'MY_NAME'
            })

        content = self.holder.get_content()['when']

        self.assertEqual(True, 'MY_NAME' in str(content))