from django.test import TestCase

from rockit.core.holders import Holder

class HolderTestCase(TestCase):

    def setUp(self):
        self.holder = Holder()

    def test_it_should_be_able_to_append(self):
        self.holder.append('TEST-01')
        self.assertEqual(True, 'TEST-01' in str(self.holder.get_content()))

    def test_content_should_be_a_dict(self):
        self.assertTrue(isinstance(self.holder.get_content(), dict))

    def test_content_should_contain_data(self):
        self.assertTrue('data' in self.holder.get_content())

    def test_data_should_contain_same_as_appended(self):
        self.holder.append('TEST-01')
        self.holder.append('TEST-02')

        data = self.holder.get_content()['data']

        self.assertEqual(2, len(data))
        self.assertEqual('TEST-01', data[0])
        self.assertEqual('TEST-02', data[1])