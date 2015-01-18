from django.test import TestCase

from rockit.core import holders

class ErrrorHolderTestCase(TestCase):

    def setUp(self):
        self.holder = holders.ErrorHolder()

    def test_it_should_be_able_to_add_error(self):
        self.holder.add_error('error_code', 'error_message');

        self.assertEqual(1, len(self.holder.get_errors()))

    def test_it_should_be_same_error_code_and_message_when_added(self):
        self.holder.add_error('error_code', 'error_message');

        self.assertTrue('error_code' in self.holder.get_errors()[0])
        self.assertEqual('error_message', self.holder.get_errors()[0]['error_code'])

    def test_it_should_be_able_to_determine_errors(self):
        self.holder.add_error('error_code', 'error_message');

        self.assertTrue(self.holder.has_errors())

    def test_it_should_not_set_errors_if_no_errors_exists(self):
        self.assertFalse(self.holder.has_errors())