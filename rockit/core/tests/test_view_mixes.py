from django.test import TestCase

from rockit.core import views

class WhenViewSetTestCase(TestCase):

    def setUp(self):
        self.views = views.MixesViewSet()
