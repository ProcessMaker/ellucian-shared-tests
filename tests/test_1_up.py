#!/usr/local/bin/python3

import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_parent import BaseTest
from util import run_test, login


class TestLoginPage(BaseTest):
    ''' Class to run test that page loads after login. '''

    def test_login(self):
        ''' Test that landing page loads. '''
        # Login using configured url, workspace, username, and password
        self.driver = login(data, self.driver)
        
        # Wait for Processes page to load
        self.wait.until(EC.visibility_of_element_located((By.ID, 'SETUP')))
        
        # Verify that Processes page elements have loaded
        self.assertTrue(self.driver.find_element_by_id('pm_main_table'))
        self.assertTrue(self.driver.find_element_by_id('pm_header'))
        self.assertTrue(self.driver.find_element_by_class_name('Footer'))


if __name__ == "__main__":
    import __main__
    try:
        output = run_test(TestLoginPage, data, __main__)
    except:
        output = {"result": "FAIL", "message": "Unkown Python Error"}
