import logging
import json
import os
import requests

from django.test import TestCase

from mock import patch

from rockit.plugins.razberry import constants
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

    def test_it_should_not_be_able_to_get_data_if_server_not_set(self):
        self.assertEqual(None, self.service.data())

    @patch('requests.get')
    def test_it_should_be_able_to_get_data(self, get): 
        models.Setting.objects.create(name=constants.SETTING_SERVER_ADDRRESS, value='localhost')
        self.assertNotEqual(None, self.service.data())

