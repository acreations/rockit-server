from django.test import TestCase

from rockit.plugins.razberry import actions

class ActionBuilderTestCase(TestCase):

    def setUp(self):
        self.builder = actions.ActionBuilder(dict())

    def test_it_should_not_be_able_to_build_action_if_device_id_is_none(self):
        holder = list()

        self.assertEqual(holder, self.builder.filter_actions_by_command_classes(None, holder))

    def test_it_should_not_be_able_to_build_action_if_holder_is_none(self):
        self.assertEqual(None, self.builder.filter_actions_by_command_classes('TEST_ID', None))