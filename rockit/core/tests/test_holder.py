from django.test import TestCase

from rockit.core.holders import Holder

class HolderTestCase(TestCase):

    def setUp(self):
        self.holder = Holder()

    def test_content_should_be_a_dictionary(self):
        self.assertTrue(isinstance(self.holder.get_content(), dict))

    def test_content_should_contain_data(self):
        self.assertNotEqual(None, self.holder.get_content())

    def test_it_should_be_able_to_append(self):
        self.holder.append('TEST-01')
        self.assertEqual(True, 'TEST-01' in str(self.holder.get_content()))

    def test_it_should_contain_Same_as_appended(self):
        self.holder.append('TEST-01')
        self.holder.append('TEST-02')

        items = self.holder.get_content()['items']

        self.assertEqual(2, len(items))
        self.assertEqual('TEST-01', items[0])
        self.assertEqual('TEST-02', items[1])

    def test_it_should_extend_if_trying_to_append_a_list(self):
        self.holder.append(['TEST-01'])
        self.holder.append(['TEST-02'])

        self.assertEqual(2, len(self.holder.get_content()['items']))

    def test_it_should_be_able_to_extend_another_holder(self):
        self.holder.append('TEST-01')

        holder = Holder()
        holder.append('TEST-02')

        self.holder.extend(holder)
        self.assertEqual(2, len(self.holder.get_content()['items']))

    def test_it_should_be_able_to_set_another_group(self):
        self.holder.append('TEST-01', 'MY_GROUP')
        self.holder.append('TEST-02', 'MY_GROUP')

        self.assertTrue('items' not in self.holder.get_content())
        self.assertEqual(2, len(self.holder.get_content()['MY_GROUP']))

    def test_it_should_be_able_to_extend_with_group(self):
        self.holder.append('TEST-01', 'MY_GROUP')
        self.holder.append('TEST-02', 'MY_GROUP')

        self.assertEqual(2, len(self.holder.get_content()['MY_GROUP']))

    def test_it_should_be_able_to_extend_another_holder_with_same_group(self):
        self.holder.append('TEST-01', 'MY_GROUP')

        holder = Holder()
        holder.append('TEST-02', 'MY_GROUP')

        self.holder.extend(holder)
        self.assertEqual(2, len(self.holder.get_content()['MY_GROUP']))

    def test_it_should_be_able_to_reset_holder(self):
        self.holder.append('TEST-01')
        self.assertEqual(1, len(self.holder.get_content()['items']))

        self.holder.reset()
        self.assertTrue('items' not in self.holder.get_content())

    def test_it_should_be_able_to_consume_contents_from_holder(self):
        self.holder.append('TEST-01')

        content = self.holder.consume()['items']

        self.assertEqual(1, len(content))
        self.assertTrue('items' not in self.holder.get_content())

    def test_it_should_be_able_to_reset_a_specific_group(self):
        self.holder.append('TEST-01', 'MY_GROUP')
        self.assertEqual(1, len(self.holder.get_content()['MY_GROUP']))

        self.holder.reset_group('MY_GROUP')

        self.assertEqual(0, len(self.holder.get_content()['MY_GROUP']))

    def test_it_should_handle_none_when_trying_to_reset_group(self):
        self.holder.reset_group(None)
