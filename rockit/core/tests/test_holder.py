from django.test import TestCase

from rockit.core.holders import Holder

class HolderTestCase(TestCase):

    def setUp(self):
        self.holder = Holder()

