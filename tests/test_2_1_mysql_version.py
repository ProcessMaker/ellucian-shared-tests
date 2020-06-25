#!/usr/local/bin/python3

import unittest
import json
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_parent import BaseTest
from util import run_test, login, read_from_json_file


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
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Case List Cache Builder')]")))
        self.driver.find_element_by_xpath("//span[contains(text(),'Case List Cache Builder')]").click()
        self.wait.until(EC.visibility_of_element_located((By.ID, 'setup-frame')))
        self.driver.switch_to.frame(self.driver.find_element_by_id('setup-frame'))

        # Get version values displayed on System Info page
        self.wait.until(EC.visibility_of_element_located((By.ID, 'ext-gen12')))
        cache_info = self.driver.find_element_by_id('ext-gen12').text
        mysql = re.search(r'(?<=MySQL Version\s)([^\s]+)(?=-)', cache_info).group(0)
        
        # Get expected RDS versions from expected_values.json
        expected_versions = read_from_json_file(self.driver.data['repository_path'],
                                                '/includes/expected_values.json', 'RDS')
        
        # Verify versions match expected
        # Assert MySQL version
        self.assertTrue(expected_versions['mysql'] in mysql)


if __name__ == "__main__":
    import __main__
    data['repository_path'] = repository_path
    output = run_test(TestComponentVersions, data, __main__)
