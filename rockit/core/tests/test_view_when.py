from django.test import TestCase

from rockit.core.views import WhenViewSet

class WhenViewSetTestCase(TestCase):

    def setUp(self):
        self.views = WhenViewSet()
