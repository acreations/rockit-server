from django.test import TestCase

from rockit.core.holders import WhenHolder
from rockit.core.models import Association

class SettingsHolderTestCase(TestCase):

    def setUp(self):
        self.association = Association.objects.create(name = 'my_node', namespace='test')

        self.holder = WhenHolder(self.association)

    def test_it_should_be_able_to_add(self):
        self.holder.add(**{
            'identifier': 1,
            'name': 'MY_NAME'
            })

        content = self.holder.get_content()

        self.assertEqual(True, 'MY_NAME' in str(content))
