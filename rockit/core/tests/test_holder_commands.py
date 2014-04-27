from django.test import TestCase

from rockit.core.holders import CommandsHolder

class CommandsHolderTestCase(TestCase):

    def setUp(self):
        self.holder = CommandsHolder()
