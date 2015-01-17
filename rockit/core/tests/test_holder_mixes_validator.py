from django.test import TestCase

from rockit.core import holders

class MixesValidationHolderTestCase(TestCase):

    def setUp(self):
        self.holder = holders.MixesValidationHolder()

    def _get_content(self):
        return self.holder.get_content()['items'];

    def test_it_should_be_able_to_add_error(self):
        self.holder.add_error('error_code', 'error_message');

        self.assertEqual(1, len(self._get_content()))

    def test_it_should_be_same_error_code_and_message_when_added(self):
        self.holder.add_error('error_code', 'error_message');

        self.assertTrue('error_code' in self._get_content()[0])
        self.assertEqual('error_message', self._get_content()[0]['error_code'])

    def test_it_should_be_able_to_determine_errors(self):
        self.holder.add_error('error_code', 'error_message');

        self.assertTrue(self.holder.has_errors())

    def test_it_should_not_set_errors_if_no_errors_exists(self):
        self.assertFalse(self.holder.has_errors())