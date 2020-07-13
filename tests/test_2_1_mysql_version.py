#!/usr/local/bin/python3

import unittest
import json
import re
from test_parent import BaseTest
from util import run_test, login, read_from_json_file
from login_page import LoginPage
from admin_page import AdminPage


class TestRDSVersions(BaseTest):
    ''' Class to navigate to Admin / Case List Cache Builder page. '''

    def test_component_version(self):
        ''' Test that MySQL version is correct. '''

        self.driver = LoginPage(self.driver, self.data).login()
        
        cache_info = AdminPage(self.driver, self.data).get_case_list_cache_builder()
        mysql = re.search(r'(?<=MySQL Version\s)([^\s]+)(?=-)', cache_info).group(0)
        
        # Get expected RDS versions from expected_values.json
        expected_versions = read_from_json_file(self.driver.data['repository_path'],
                                                '/includes/expected_values.json', 'RDS')
        
        # Verify versions match expected
        # Assert MySQL version
        try:
            self.assertTrue(expected_versions['mysql'] in mysql)
            self.log.append('Correct MySQL version')
        except:
            self.log.append('Wrong MySQL version')
            self.fail()


if __name__ == "__main__":
    import __main__
    data['repository_path'] = repository_path
    output = run_test(TestRDSVersions, data, __main__)