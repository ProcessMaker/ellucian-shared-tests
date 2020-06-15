#!/usr/local/bin/python3

import unittest
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

        # Verify correct Plugin versions present
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'x-grid3')))
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'x-grid3-row')))
        from time import sleep
        sleep(1)
        plugins = ' '.join([element.text for element in self.driver.find_elements_by_class_name('x-grid3-row')])
        for key, val in self.driver.data['plugins'].items():
            self.assertTrue(val in plugins)
            self.assertTrue(key in plugins)


if __name__ == "__main__":
    import __main__
    # Assign plugin version variables
    data['plugins'] = {
        "Ellucian Ethos Events": "1.3.0+012",
        "SSO_SAML": "3.2.5",
        "Ellucian Ethos Integration": "1.5.0+950",
        "pmBusinessRules": "3.1.3"
    }
    # STM plugin version unknown
    output = run_test(TestPluginVersions, data, __main__)
