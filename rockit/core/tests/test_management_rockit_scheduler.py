from django.test import TestCase

from rockit.core.management.commands.rockitscheduler import Command

class RockitSchedulerTestCase(TestCase):

    def setUp(self):
        self.command = Command()

    def test_it_should_be_able_to_handle_command(self):
        self.command.handle()