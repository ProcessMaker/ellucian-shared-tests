#!/usr/local/bin/python3

import unittest
import json
import re
from test_parent import BaseTest
from util import run_test, read_from_json_file
from login_page import LoginPage
from admin_page import AdminPage


class TestRDSVersions(BaseTest):
    ''' Class to navigate to Admin / Case List Cache Builder page. '''

    def test_component_version(self):
        ''' Test that MySQL version is correct. '''

        self.driver = LoginPage(self.driver, self.data).login()

        html = AdminPage(self.driver, self.data).get_case_list_cache_builder()
        if html:
            mysql = re.search(r'(?<=MySQL Version\s)([^\s]+)(?=-)', html).group(0)

        # Get expected RDS versions from expected_values.json
        expected_versions = read_from_json_file(self.data['repository_path'],
                                                '/includes/expected_values.json', 'RDS')

        # Verify versions match expected
        # Assert MySQL version
        try:
            self.assertTrue(expected_versions['mysql'] in mysql)
            self.log.append('Correct MySQL version: ' + expected_versions['mysql'])
        except:
            self.log.append('Incorrect MySQL version: ' + mysql + ', Expected: ' + expected_versions['mysql'])
            self.fail()


if __name__ == "__main__":
    import __main__
    data['repository_path'] = repository_path
    output = run_test(TestRDSVersions, data, __main__)
