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
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Admin')))
        
        # Navigate to Admin / System Info page
        self.driver.find_element_by_id('SETUP').click()
        self.wait.until(EC.visibility_of_element_located((By.ID, 'adminFrame')))
        self.driver.switch_to.frame(self.driver.find_element_by_id('adminFrame'))
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'System information')))
        self.driver.find_element_by_link_text('System information').click()
        self.wait.until(EC.visibility_of_element_located((By.ID, 'setup-frame')))
        self.driver.switch_to.frame(self.driver.find_element_by_id('setup-frame'))

        # Get version values displayed on System Info page
        self.wait.until(EC.visibility_of_element_located((By.ID, 'ext-gen13-gp-section-Process Information-bd')))
        self.wait.until(EC.visibility_of_element_located((By.ID, 'ext-gen13-gp-section-System information-bd')))
        self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'x-grid3-row')))
        process_info = self.driver.find_element_by_id('ext-gen13-gp-section-Process Information-bd').text
        system_info = self.driver.find_element_by_id('ext-gen13-gp-section-System information-bd').text
        pm3 = re.search(r'(?<=ProcessMaker Ver.\s)([^\s]+)', process_info).group(0)
        mysql = re.search(r'(?<=MySql \(Version\s)([^\s]+)(?=\))', process_info).group(0)
        nginx = re.search(r'(?<=nginx/)([^\s]+)', system_info).group(0)
        php = re.search(r'(?<=PHP Version\s)([^\s]+)', system_info).group(0)

        # Get expected System Information versions from expected_values.json
        expected_versions = read_from_json_file(self.driver.data['repository_path'],
                                                '/includes/expected_values.json', 'System Information')

        # Verify versions match expected
        # Assert PM3 version
        self.assertTrue(expected_versions['pm3'] in pm3)
        # Assert MySql version
        self.assertTrue(expected_versions['mysql'] in mysql) 
        # Assert Nginx version
        self.assertTrue(expected_versions['nginx'] in nginx)
        # Assert PHP version
        self.assertTrue(expected_versions['php'] in php)


if __name__ == "__main__":
    import __main__
    data['repository_path'] = repository_path
    output = run_test(TestComponentVersions, data, __main__)
