from django.test import TestCase

from rockit.core.holders import CommandsHolder

class DetailsHolderTestCase(TestCase):

    def setUp(self):
        self.holder = CommandsHolder()
