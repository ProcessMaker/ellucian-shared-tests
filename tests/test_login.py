#!/usr/local/bin/python3

import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_parent import BaseTest
from util import run_test, login


class TestCorrectCredentials(BaseTest):
    ''' Class to run test that correct login credentials work. '''

    def test_correct_credentials(self):
        ''' Test that correct credentials work. '''
        # Login using configured url, workspace, username, and password
        self.driver = login(data, self.driver)
        
        # Wait for Processes page to load
        self.wait.until(EC.visibility_of_element_located((By.ID, 'SETUP')))
        self.wait.until(EC.visibility_of_element_located((By.ID, 'adminFrame')))
        
        # Verify that Processes page elements have loaded
        self.assertTrue(self.driver.find_element_by_id('pm_main_table'))
        self.assertTrue(self.driver.find_element_by_id('pm_header'))
        self.assertTrue(self.driver.find_element_by_class_name('Footer'))
        self.assertTrue(self.driver.find_element_by_id('adminFrame'))
        self.driver.switch_to.frame(self.driver.find_element_by_id('adminFrame'))
        self.assertTrue(self.driver.find_element_by_id('west-panel'))
        self.assertTrue(self.driver.find_element_by_id('mif-comp-1002'))
        self.assertTrue(self.driver.find_element_by_id('setup-frame'))
        


if __name__ == "__main__":
    import __main__
    output = run_test(TestCorrectCredentials, data, __main__)
