#!/usr/local/bin/python3

import unittest
import json
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_parent import BaseTest
from util import run_test, login, read_from_json_file


class TestRDSVersions(BaseTest):
    ''' Class to navigate to Admin / Case List Cache Builder page. '''

    def test_component_version(self):
        ''' Test that MySQL version is correct. '''

        self.driver = login(data, self.driver)
        
        # Navigate to Admin / Case List Cache Builder page
        self.wait.until(EC.visibility_of_element_located((By.ID, 'SETUP'))).click()
        self.wait.until(EC.visibility_of_element_located((By.ID, 'adminFrame')))
        self.driver.switch_to.frame(self.driver.find_element_by_id('adminFrame'))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Case List Cache Builder')]"))).click()
        self.wait.until(EC.visibility_of_element_located((By.ID, 'setup-frame')))
        self.driver.switch_to.frame(self.driver.find_element_by_id('setup-frame'))

        # Get version values displayed on Case List Cache Builder page
        self.wait.until(EC.visibility_of_element_located((By.ID, 'ext-gen12')))
        from time import sleep
        sleep(1)
        cache_info = self.driver.find_element_by_id('ext-gen12').text
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

        self.log = self.driver.log

if __name__ == "__main__":
    import __main__
    data['repository_path'] = repository_path
    output = run_test(TestRDSVersions, data, __main__)
