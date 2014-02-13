from django.test import TestCase

from rockit.foundation.core.holders.settings import SettingsHolder

class SettingsHolderTestCase(TestCase):

    def setUp(self):
        self.holder = SettingsHolder()

    def test_it_should_be_able_add_settings(self):
        self.holder.add_setting('MY_KEY', 'MY_NAME', 'MY_VALUE')

        content = self.holder.get_content()

        self.assertEqual(1, len(content))
        self.assertEqual(True, 'MY_KEY' in str(content))
        self.assertEqual(True, 'MY_NAME' in str(content))
        self.assertEqual(True, 'MY_VALUE' in str(content))

    def test_it_should_be_able_to_generate_a_settings(self):
    	setting = self.holder.generate_setting('MY_KEY', 'MY_NAME', 'MY_VALUE')

        self.assertEqual(True, 'MY_KEY' in str(setting))
        self.assertEqual(True, 'MY_NAME' in str(setting))
        self.assertEqual(True, 'MY_VALUE' in str(setting))

    def test_it_should_be_able_to_add_group_of_settings(self):
    	settings = [
    		self.holder.generate_setting('MY_KEY1', 'MY_NAME1', 'MY_VALUE1'),
    		self.holder.generate_setting('MY_KEY2', 'MY_NAME2', 'MY_VALUE2'),
    		self.holder.generate_setting('MY_KEY3', 'MY_NAME3', 'MY_VALUE3')
    	]

    	self.holder.add_setting_group('MY_GROUP', settings)

    	content = self.holder.get_content()

    	self.assertEqual(1, len(content))
    	self.assertEqual(True, 'MY_GROUP' in str(content))