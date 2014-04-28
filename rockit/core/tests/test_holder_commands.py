from django.test import TestCase

from rockit.core.holders import CommandsHolder

class CommandsHolderTestCase(TestCase):

    def setUp(self):
        self.holder = CommandsHolder()

    def test_it_should_be_able_to_add_switch_command(self):
        self.holder.add_switch_command('IDENTIFIER', 'TEST_BINARY', 'true', 'false', 'false')

        content = self.holder.get_content()

        self.assertEqual(True, 'IDENTIFIER' in str(content))
        self.assertEqual(True, 'TEST_BINARY' in str(content))
        self.assertEqual(True, 'on' in str(content))
        self.assertEqual(True, 'off' in str(content))
        self.assertEqual(True, 'current' in str(content))

    def test_it_should_be_able_to_add_choice_command(self):
        self.holder.add_choice_command('TEST_CHOICE')

        # Add more unit test later

    def test_it_should_be_able_to_add_scales_command(self):
        self.holder.add_scales_command('TEST_SCALES')

        # Add more unit test later