#!/usr/local/bin/python3

import unittest
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_parent import BaseTest
from util import run_test, read_from_json_file
from login_page import LoginPage
from admin_page import AdminPage


class TestPluginVersions(BaseTest):
    ''' Class to navigate to Admin / Plugins Manager page. '''

    def setUp(self):
        self.assertionFailures = []

    def tearDown(self):
        self.assertEqual([], self.assertionFailures)

    def test_plugin_versions(self):
        ''' Test that versions are correct. '''

        self.driver = LoginPage(self.driver, self.data).login()

        # Retrieve Custom Plugins dictionary from expected_values.json
        custom_plugins = read_from_json_file(self.data['repository_path'],
                                             '/includes/expected_values.json', 'Custom Plugins')

        # Verify all custom plugins are visible on page with correct version, and are enabled
        plugins = AdminPage(self.driver, self.data).get_plugins()

        self.driver.log.append('Plugin versions: ')
        for elem in plugins:
            for key in custom_plugins.keys():
                if key in elem:
                    try:
                        self.assertTrue(custom_plugins[key] in elem)
                        self.driver.log[-1] += 'Correct ' + key + ', '
                    except AssertionError as e:
                        self.driver.log[-1] += 'Wrong ' + key + ' version, '
                        self.assertionFailures.append(str(e))

                    del custom_plugins[key]
                    break 
        
        # Assert custom_plugins is empty (meaning every expected value was found)
        try:
            self.assertEqual(custom_plugins, {})
            self.driver.log[-1] += 'All found'
        except AssertionError as e:
            not_found = ', '.join(custom_plugins)
            self.driver.log[-1] += 'Not found: ' + not_found
            self.assertionFailures.append(str(e))


if __name__ == "__main__":
    import __main__
    data['repository_path'] = repository_path
    output = run_test(TestPluginVersions, data, __main__)
