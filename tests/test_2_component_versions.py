#!/usr/local/bin/python3

import unittest
import json
import re
from test_parent import BaseTest
from util import run_test, read_from_json_file
from page import *


class TestComponentVersions(BaseTest):
    ''' Class to navigate to Admin / System Info page. '''

    def setUp(self):
        ''' Run before each test method. '''
        login_page = LoginPage(self.driver, data)
        self.assertTrue(login_page.login())
        self.assertionFailures = []

    def tearDown(self):
        ''' Run after each test method. '''
        self.assertEqual([], self.assertionFailures)

    def test_component_version(self):
        ''' Test that versions are correct. '''

        process_info, system_info = AdminPage(self.driver, self.data).get_system_information()

        pm3 = re.search(r'(?<=ProcessMaker Ver.\s)([^\s]+)', process_info).group(0)
        nginx = re.search(r'(?<=nginx/)([^\s]+)', system_info).group(0)
        php = re.search(r'(?<=PHP Version\s)([^\s]+)', system_info).group(0)

        # Get expected System Information versions from expected_values.json
        expected_versions = read_from_json_file(data['repository_path'],
                                                '/includes/expected_values.json', 'System Information')

        # Verify versions match expected
        try:
            # Assert PM3 version
            self.assertTrue(expected_versions['pm3'] in pm3)
            self.driver.log.append('Correct ProcessMaker version: ' + pm3 +\
                ' ---------- ')
        except AssertionError as e:
            self.driver.log.append('Incorrect ProcessMaker version: ' + pm3 +\
                ', Expected: ' + expected_versions['pm3'] + ' ---------- ')
            self.assertionFailures.append(str(e))

        try:
            # Assert Nginx version
            self.assertTrue(expected_versions['nginx'] in nginx)
            self.driver.log[-1] += 'Correct Nginx version: ' + nginx + ' ---------- '
        except AssertionError as e:
            self.driver.log[-1] += 'Incorrect Nginx version: ' + nginx + ', Expected: ' +\
                expected_versions['nginx'] + ' ---------- '
            self.assertionFailures.append(str(e))

        try:
            # Assert PHP version
            self.assertTrue(expected_versions['php'] in php)
            self.driver.log[-1] += 'Correct PHP version: ' + php
        except AssertionError as e:
            self.driver.log[-1] += 'Incorrect PHP version: ' + php + ', Expected: ' +\
                expected_versions['php']
            self.assertionFailures.append(str(e))


if __name__ == "__main__":
    import __main__
    data['repository_path'] = repository_path
    output = run_test(TestComponentVersions, data, __main__)
