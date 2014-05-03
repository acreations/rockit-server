from django.test import TestCase

from rockit.plugins.razberry import resolvers

class ValueResolverTestCase(TestCase):

    def setUp(self):
        self.resolver = resolvers.ValueResolver()

    def test_it_should_not_be_able_to_resolve_null_command(self):
        self.assertEqual(None, self.resolver.resolve_command_value(None))

    def test_it_should_return_none_if_command_is_unsupported(self):
        self.assertEqual(None, self.resolver.resolve_command_value({
            'name': 'NOT_SUPPORTED'
            }))

    def test_it_should_return_supported_switch_binary_command(self):
        self.assertNotEqual(None, self.resolver.resolve_command_value({
            'name': 'SwitchBinary'
            }))