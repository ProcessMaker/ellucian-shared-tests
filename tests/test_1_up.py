#!/usr/local/bin/python3

import unittest
from io import StringIO
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_parent import BaseTest
from util import run_test, login


class TestLoginPage(BaseTest):
    ''' Class to run test that page loads after login. '''

    def test_login(self):
        ''' Test that landing page loads. '''

        self.driver = login(data, self.driver, self.log)

        # Wait for Processes page to load
        self.driver.log.append('Waiting for main page to load')
        self.wait.until(EC.visibility_of_element_located((By.ID, 'SETUP')))

        # Verify that Processes page elements have loaded
        try:
            self.assertTrue(self.driver.find_element_by_id('pm_main_table'))
            self.assertTrue(self.driver.find_element_by_id('pm_header'))
            self.assertTrue(self.driver.find_element_by_class_name('Footer'))
            self.driver.log.append('Main page loaded successfully')
        except: 
            self.driver.log.append('Main page failed to load')
            self.fail()

        self.log = self.driver.log


if __name__ == "__main__":
    import __main__
    output = run_test(TestLoginPage, data, __main__)
