from django.test import TestCase

from rockit.core import holders
from rockit.core import models

class MixesHolderTestCase(TestCase):

    def setUp(self):
        self.association = models.Association.objects.create(name = 'my_node', namespace='test')

        self.holder = holders.MixesHolder(self.association)

    def test_it_should_be_able_to_add(self):
        self.holder.add_when(**{
            'identifier': 1,
            'name': 'MY_NAME'
            })

        content = self.holder.get_content()

        self.assertEqual(True, 'MY_NAME' in str(content))
