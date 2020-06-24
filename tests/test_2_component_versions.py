#!/usr/local/bin/python3

import unittest
import json
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_parent import BaseTest
from util import run_test, login


class TestComponentVersions(BaseTest):
    ''' Class to navigate to Admin / System Info page. '''

    def test_component_version(self):
        ''' Test that versions are correct. '''
        # Login using configured url, workspace, username, and password
        self.driver = login(data, self.driver)
        
        # Wait for Processes page to load
        self.wait.until(EC.visibility_of_element_located((By.ID, 'SETUP')))
        
        # Navigate to Admin / System Info page
        self.driver.find_element_by_id('SETUP').click()
        self.wait.until(EC.visibility_of_element_located((By.ID, 'adminFrame')))
        self.driver.switch_to.frame(self.driver.find_element_by_id('adminFrame'))
        self.wait.until(EC.visibility_of_element_located((By.ID, 'extdd-34')))
        self.driver.find_element_by_id('extdd-34').click()
        self.wait.until(EC.visibility_of_element_located((By.ID, 'setup-frame')))
        self.driver.switch_to.frame(self.driver.find_element_by_id('setup-frame'))

        with open(self.driver.data['repository_path'] + '/includes/expected_values.json') as expectedValuesFile:
            expected_values = json.loads(expectedValuesFile.read())

        expected_versions = expected_values[0]['System Information']

        # Verify correct versions in Process Info and System Info
        self.wait.until(EC.visibility_of_element_located((By.ID, 'ext-gen13-gp-section-Process Information-bd')))
        self.wait.until(EC.visibility_of_element_located((By.ID, 'ext-gen13-gp-section-System information')))
        process_info = self.driver.find_element_by_id('ext-gen13-gp-section-Process Information-bd').text
        system_info = self.driver.find_element_by_id('ext-gen13-gp-section-System information').text
        print(system_info)
        pm3 = re.search(r'(?<=ProcessMaker Ver.\s)([^\s]+)', process_info).group(0)
        nginx = re.search(r'(?<=nginx/)([^\s]+)', system_info).group(0)
        php = re.search(r'(?<=PHP Version\s)([^\s]+)', system_info).group(0)

        # Assert PM3 version
        self.assertTrue(expected_versions['pm3'] in pm3)
        # Assert MySQL version -- currently not visible in same location
        # self.assertTrue(self.driver.data['mysql'] in versions[6].text)
        # Assert Nginx version
        self.assertTrue(expected_versions['nginx'] in nginx)
        # Assert PHP version
        self.assertTrue(expected_versions['php'] in php)
        


if __name__ == "__main__":
    import __main__
    # Assign component version variables
    data['repository_path'] = repository_path
    output = run_test(TestComponentVersions, data, __main__)
