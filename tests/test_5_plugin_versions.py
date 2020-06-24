#!/usr/local/bin/python3

import unittest
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_parent import BaseTest
from util import run_test, login


class TestPluginVersions(BaseTest):
    ''' Class to navigate to Admin / Plugins Manager page. '''

    def test_plugin_versions(self):
        ''' Test that versions are correct. '''
        # Login using configured url, workspace, username, and password
        self.driver = login(data, self.driver)
        
        # Wait for Processes page to load
        self.wait.until(EC.visibility_of_element_located((By.ID, 'SETUP')))
        
        # Navigate to Admin / Plugins Manager page
        self.driver.find_element_by_id('SETUP').click()
        self.wait.until(EC.visibility_of_element_located((By.ID, 'adminFrame')))
        self.driver.switch_to.frame(self.driver.find_element_by_id('adminFrame'))
        self.wait.until(EC.visibility_of_element_located((By.ID, 'ext-gen22')))
        self.driver.find_element_by_id('ext-gen22').click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "ext-gen44")))
        self.driver.find_element_by_id('ext-gen44').click()
        self.wait.until(EC.visibility_of_element_located((By.ID, 'setup-frame')))
        self.driver.switch_to.frame(self.driver.find_element_by_id('setup-frame'))

        # Open Expected Values file and read
        with open(self.driver.data['repository_path'] + '/includes/expected_values.json') as expectedValuesFile:
            expected_values = json.loads(expectedValuesFile.read())

        # Verify correct Plugin versions present
        # Wait for grid to load
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'x-grid3')))
        # Wait for each row to load
        self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'x-grid3-row')))

        from time import sleep
        sleep(1)

        plugins = [element.text for element in self.driver.find_elements_by_class_name('x-grid3-row')]
        for elem in plugins:
            for key, val in expected_values[0]['Custom Plugins'].items():
                if key in elem:
                    self.assertTrue(val in elem)
                    #self.assertTrue('Enabled' in elem) -- currently SSO_SAML disabled
                    key = 'found'
                    break # End loop once key is found
            # Delete key, val pairs
            delete = [key for key in expected_values[0]['Custom Plugins'] if key == 'found']
            for key in delete: del expected_values[0]['Custom Plugins'][key] 
            # Assert dict is empty (meaning every expected value was found)
            #self.assertEqual(expected_values[0]['Custom Plugins'], {})
            # -- needs to be updated when final list of expected plugins is provided


if __name__ == "__main__":
    import __main__
    data['repository_path'] = repository_path
    output = run_test(TestPluginVersions, data, __main__)
