from django.test import TestCase

from rockit.core.holders import Holder

class HolderTestCase(TestCase):

    def setUp(self):
        self.holder = Holder()

    def test_it_should_be_able_to_append(self):
        self.holder.append('TEST-01')
        self.holder.append('TEST-02')
        self.holder.append('TEST-03')
        self.holder.append('TEST-04')
        self.holder.append('TEST-05')

        content = self.holder.get_content()

        self.assertEqual(True, 'TEST-01' in str(content))
        self.assertEqual(True, 'TEST-02' in str(content))
        self.assertEqual(True, 'TEST-03' in str(content))
        self.assertEqual(True, 'TEST-04' in str(content))
        self.assertEqual(True, 'TEST-05' in str(content))