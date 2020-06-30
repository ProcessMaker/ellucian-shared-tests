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
        # Login using configured url, workspace, username, and password
        self.log.append('Attempting login...')
        self.driver = login(data, self.driver, self.log)

        # Wait for Processes page to load
        self.driver.log.append('Waiting for main page to load')
        self.wait.until(EC.visibility_of_element_located((By.ID, 'SETUP')))

        # Verify that Processes page elements have loaded
        self.assertTrue(self.driver.find_element_by_id('pm_main_table'))
        self.assertTrue(self.driver.find_element_by_id('pm_header'))
        self.assertTrue(self.driver.find_element_by_class_name('Footer'))

        self.driver.log.append('Test passed')
        self.log = self.driver.log
        if self.driver.page:
            self.page = self.driver.page


if __name__ == "__main__":
    import __main__
    output = run_test(TestLoginPage, data, __main__)
