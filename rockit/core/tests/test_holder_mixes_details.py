from django.test import TestCase

from rockit.core import holders

class MixesDetailsHolderTestCase(TestCase):

    def setUp(self):
        self.holder = holders.MixesDetailsHolder()

        self.example = {
            'identifier': 'TEST',
            'type': 'TEST_TYPE',
            'required': True,
            'label': 'TEST_LABEL',
            'max_length': 100
            }

    def test_it_should_contain_actions_class(self):
        self.assertTrue('actions' in self.holder.get_content())

    def test_it_should_contain_post_when_using_add_post(self):
        self.holder.add_post(**self.example)

        self.assertTrue('POST' in self.holder.get_content()['actions'])

    def test_it_should_contain_put_when_using_add_update(self):
        self.holder.add_update(**self.example)

        self.assertTrue('PUT' in self.holder.get_content()['actions'])

    def test_it_should_contain_post_when_added_post_items(self):
        self.holder.add_post(**self.example)

        post = self.holder.get_content()['actions']['POST']
        self.assertTrue('TEST' in post)
        self.assertTrue('type' in post['TEST'])
        self.assertTrue('required' in post['TEST'])
        self.assertTrue('label' in post['TEST'])
        self.assertTrue('max_length' in post['TEST'])

        self.assertEqual('TEST_TYPE', post['TEST']['type'])
        self.assertEqual(True, post['TEST']['required'])
        self.assertEqual('TEST_LABEL', post['TEST']['label'])
        self.assertEqual(100, post['TEST']['max_length'])

    def test_it_should_not_contain_required_if_not_set(self):
        del self.example['max_length']
        
        self.holder.add_post(**self.example)

        self.assertTrue('max_length' not in self.holder.get_content()['actions']['POST']['TEST'])