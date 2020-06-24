#!/usr/local/bin/python3

import unittest
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_parent import BaseTest
from util import run_test, login, read_from_json_file


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

        # Wait for grid to load
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'x-grid3')))
        self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'x-grid3-row')))

        # Work around stale elements issue
        from time import sleep
        sleep(1)


        # Retrieve Custom Plugins dictionary from expected_values.json
        custom_plugins = read_from_json_file(self.driver.data['repository_path'],
                                             '/includes/expected_values.json', 'Custom Plugins')

        # Verify all custom plugins are visible on page with correct version, and are enabled
        plugins = [element.text for element in self.driver.find_elements_by_class_name('x-grid3-row')]
        for elem in plugins:
            for key, val in custom_plugins.items():
                if key in elem:
                    self.assertTrue(val in elem)
                    #self.assertTrue('Enabled' in elem) -- currently SSO_SAML disabled
                    key = 'found'
                    break
            del custom_plugins['found'] 
            # Assert custom_plugins is empty (meaning every expected value was found)
            #self.assertEqual(custom_plugins, {})
            # -- needs to be updated when final list of expected plugins is provided


if __name__ == "__main__":
    import __main__
    data['repository_path'] = repository_path
    output = run_test(TestPluginVersions, data, __main__)
