#!/usr/local/bin/python3

import unittest
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_parent import BaseTest
from util import run_test, login, read_from_json_file
from login_page import LoginPage
from admin_page import AdminPage


class TestPluginVersions(BaseTest):
    ''' Class to navigate to Admin / Plugins Manager page. '''

    def test_plugin_versions(self):
        ''' Test that versions are correct. '''

        self.driver = LoginPage(self.driver, self.data).login()

        # Retrieve Custom Plugins dictionary from expected_values.json
        custom_plugins = read_from_json_file(self.driver.data['repository_path'],
                                             '/includes/expected_values.json', 'Custom Plugins')

        # Verify all custom plugins are visible on page with correct version, and are enabled
        plugins = AdminPage(self.driver, self.data).get_plugins()

        
        fail_flag = 0
        self.driver.log.append('Plugin versions: ')
        for elem in plugins:
            for key in custom_plugins.keys():
                if key in elem:
                    try:
                        self.assertTrue(custom_plugins[key] in elem)
                        self.driver.log[-1] += 'Correct ' + key + ', '
                    except:
                        self.driver.log[-1] += 'Wrong ' + key + ' version , '
                        fail_flag = 1
                    
                    try:
                        self.assertTrue('Enabled' in elem)
                        self.driver.log[-1] += 'Enabled; '
                    except:
                        self.driver.log[-1] += 'Disabled; '
                        fail_flag = 1

                    del custom_plugins[key]
                    break 
            # Assert custom_plugins is empty (meaning every expected value was found)
        try:
            self.assertEqual(custom_plugins, {})
            self.driver.log[-1] += 'All found'
        except:
            not_found = ', '.join(custom_plugins)
            self.driver.log[-1] += 'Not found: ' + not_found
            fail_flag = 1

        if fail_flag == 1:
            self.fail()
        self.log = self.driver.log


if __name__ == "__main__":
    import __main__
    data['repository_path'] = repository_path
    output = run_test(TestPluginVersions, data, __main__)
