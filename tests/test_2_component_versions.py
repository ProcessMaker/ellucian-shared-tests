#!/usr/local/bin/python3

import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_parent import BaseTest
from util import run_test, login


class TestComponentVersions(BaseTest):
    ''' Class to run test that page loads after login. '''

    def test_component_version(self):
        ''' Test that landing page loads. '''
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

        # Verify correct versions in Process Info and System Info
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'x-grid3-row')))
        versions = self.driver.find_elements_by_class_name('x-grid3-row')
        # Assert PM3 version
        self.assertTrue(self.driver.data['pm3'] in versions[0].text)
        # Assert MySQL version
        self.assertTrue(self.driver.data['mysql'] in versions[6].text)
        # Assert Nginx version
        self.assertTrue(self.driver.data['nginx'] in versions[12].text)
        # Assert PHP version
        self.assertTrue(self.driver.data['php'] in versions[14].text)


if __name__ == "__main__":
    import __main__
    # Assign component version variables
    data['php'] = '7.3.15'
    data['mysql'] = '5.7'
    data['nginx'] = '1.16.1'
    data['pm3'] = '3.4.11'
    output = run_test(TestComponentVersions, data, __main__)
