from django.test import TestCase

from rockit.core.holders import DetailsHolder

class DetailsHolderTestCase(TestCase):

    def setUp(self):
        self.holder = DetailsHolder()

    def test_it_should_be_able_to_add_detail(self):
        self.holder.add(**{
            'title': 'MY_TITLE',
            'value': 'MY_VALUE'
            })

        content = self.holder.get_content()

        self.assertEqual(True, 'MY_TITLE' in str(content))
        self.assertEqual(True, 'MY_VALUE' in str(content))

    def test_it_should_be_able_to_add_changeable_details(self):
        self.holder.add(**{
            'title': 'MY_TITLE',
            'value': 'MY_VALUE',
            'url': 'MY_CHANGE_URL'
            })

        content = self.holder.get_content()

        self.assertEqual(True, 'MY_TITLE' in str(content))
        self.assertEqual(True, 'MY_VALUE' in str(content))
        self.assertEqual(True, 'MY_CHANGE_URL' in str(content))