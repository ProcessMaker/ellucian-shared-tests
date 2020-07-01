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
        self.driver = login(data, self.driver, self.log)
        
        # Wait for Processes page to load
        self.wait.until(EC.visibility_of_element_located((By.ID, 'SETUP')))
        
        # Navigate to Admin / Plugins Manager page
        self.driver.find_element_by_id('SETUP').click()
        self.wait.until(EC.visibility_of_element_located((By.ID, 'adminFrame')))
        self.driver.switch_to.frame(self.driver.find_element_by_id('adminFrame'))
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Plugins')))
        self.driver.find_element_by_link_text('Plugins').click()
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Plugins Manager")))
        self.driver.find_element_by_link_text('Plugins Manager').click()
        self.wait.until(EC.visibility_of_element_located((By.ID, 'setup-frame')))
        self.driver.switch_to.frame(self.driver.find_element_by_id('setup-frame'))
        
        # Work around stale elements issue
        from time import sleep
        sleep(2)

        # Wait for grid to load
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'x-grid3')))
        self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'x-grid3-row')))

        # Retrieve Custom Plugins dictionary from expected_values.json
        custom_plugins = read_from_json_file(self.driver.data['repository_path'],
                                             '/includes/expected_values.json', 'Custom Plugins')

        # Verify all custom plugins are visible on page with correct version, and are enabled
        plugins = [element.text for element in self.driver.find_elements_by_class_name('x-grid3-row')]
        fail_flag = 0
        self.driver.log.append('Plugins: ')
        for elem in plugins:
            for key in custom_plugins.keys():
                if key in elem:
                    try:
                        self.assertTrue(custom_plugins[key] in elem)
                        self.driver.log[-1] += 'Correct ' + key + ' version , '
                    except:
                        self.driver.log[-1] += 'Wrong ' + key + ' version , '
                        fail_flag = 1
                    
                    try:
                        self.assertTrue('Enabled' in elem)
                        self.driver.log[-1] += 'Enabled; '
                    except:
                        self.driver.log[-1] += 'Disabled; '
                        fail_flag = 1

                    del custom_plugins[key]
                    break 
            # Assert custom_plugins is empty (meaning every expected value was found)
        try:
            self.assertEqual(custom_plugins, {})
            self.driver.log[-1] += 'All plugins found'
        except:
            not_found = ', '.join(custom_plugins)
            self.driver.log[-1] += 'Not found: ' + not_found
            fail_flag = 1

        if fail_flag == 1:
            self.fail()
        self.log = self.driver.log


if __name__ == "__main__":
    import __main__
    data['repository_path'] = repository_path
    output = run_test(TestPluginVersions, data, __main__)
