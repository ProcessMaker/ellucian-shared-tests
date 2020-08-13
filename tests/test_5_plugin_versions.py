#!/usr/local/bin/python3

import unittest
import json
from test_parent import BaseTest
from util import run_test, read_from_json_file
from page import *


class TestPluginVersions(BaseTest):
    ''' Class to navigate to Admin / Plugins Manager page. '''

    def setUp(self):
        ''' Run before each test method. '''
        login_page = LoginPage(self.driver, data)
        login_page.go_to_page()
        login_page.login()
        self.assertionFailures = []

    def tearDown(self):
        ''' Run after each test method. '''
        self.assertEqual([], self.assertionFailures)

    def test_plugin_versions(self):
        ''' Test that versions are correct. '''

        # Retrieve Custom Plugins dictionary from expected_values.json
        custom_plugins = read_from_json_file(self.data['repository_path'],
                                             '/includes/expected_values.json', 'Custom Plugins')

        # Verify all custom plugins are visible on page with correct version, and are enabled
        plugins = AdminPage(self.driver, self.data).get_plugins()
        self.driver.log.append('')

        for elem in plugins:
            for key in custom_plugins.keys():
                if key in elem:
                    try:
                        version = re.search(r'(?<=\)\s)([^\s]+)', elem).group(0)
                        self.assertTrue(custom_plugins[key] in elem)
                        self.driver.log[-1] += 'Correct ' + key + ' version: ' + version +\
                            ' ---------- '
                    except AssertionError as e:
                        self.driver.log[-1] += 'Incorrect ' + key + ' version: ' +\
                            version + ', Expected: ' + custom_plugins[key] + ' ---------- '
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
