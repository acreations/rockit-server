import logging
import json
import os

from django.test import TestCase

from rockit.plugins.razberry import models
from rockit.plugins.razberry.services import RazberryService

class ParsingTestCase(TestCase):

    logger = logging.getLogger(__name__)

    def setUp(self):
        self.service = RazberryService()

    def test_it_should_normalize_namespace_correctly(self):
        namespace = 'devices.3.instances.0.commandClasses.37.data'
        normalize = self.service.normalize(namespace)

        self.assertEqual('devices[3].instances[0].commandClasses[0x25].data', normalize)

    def test_it_should_normalize_even_when_no_index_are_provided(self):
        namespace = 'devices.instances.commandClasses.data'
        self.assertEqual(namespace, self.service.normalize(namespace))

        namespace = 'test'
        self.assertEqual(namespace, self.service.normalize(namespace))

    def test_it_should_return_none_if_namespace_is_empty(self):
        self.assertEqual(None, self.service.normalize(None))