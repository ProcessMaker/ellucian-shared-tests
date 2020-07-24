#!/usr/local/bin/python3

import unittest
import json
import re
from test_parent import BaseTest
from util import run_test, login, read_from_json_file
from login_page import LoginPage
from admin_page import AdminPage


class TestComponentVersions(BaseTest):
    ''' Class to navigate to Admin / System Info page. '''

    def test_component_version(self):
        ''' Test that versions are correct. '''

        self.driver = LoginPage(self.driver, self.data).login()
        
        process_info, system_info = AdminPage(self.driver, self.data).get_system_information()

        pm3 = re.search(r'(?<=ProcessMaker Ver.\s)([^\s]+)', process_info).group(0)
        nginx = re.search(r'(?<=nginx/)([^\s]+)', system_info).group(0)
        php = re.search(r'(?<=PHP Version\s)([^\s]+)', system_info).group(0)

        # Get expected System Information versions from expected_values.json
        expected_versions = read_from_json_file(data['repository_path'],
                                                '/includes/expected_values.json', 'System Information')

        fail_flag = 0
        # Verify versions match expected
        self.driver.log.append('Versions: ')
        try:
            # Assert PM3 version 
            self.assertTrue(expected_versions['pm3'] in pm3)
            self.driver.log[-1] += 'Correct ProcessMaker'
        except:
            self.driver.log[-1] += 'Wrong ProcessMaker'
            fail_flag = 1

        try:
            # Assert Nginx version
            self.assertTrue(expected_versions['nginx'] in nginx)
            self.driver.log[-1] += '; Correct Nginx'
        except:
            self.driver.log[-1] += '; Wrong Nginx'
            fail_flag = 1

        try:
            # Assert PHP version
            self.assertTrue(expected_versions['php'] in php)
            self.driver.log[-1] += '; Correct PHP'
        except:
            self.driver.log[-1] += '; Wrong PHP'
            fail_flag = 1

        if fail_flag == 1:
            self.fail()


if __name__ == "__main__":
    import __main__
    data['repository_path'] = repository_path
    output = run_test(TestComponentVersions, data, __main__)
