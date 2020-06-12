#!/usr/local/bin/python3

import unittest
from test_parent import BaseTest
from util import run_test
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestLoginPage(BaseTest):
    ''' Class to run test that login fields exist. '''

    def test_login_page(self):
        ''' Test that login page displays. '''
        # Navigate to server
        self.driver.get(data['server_url'])

        # Verify that workspace selection and submit button are displayed
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'select-workspace')))
        self.wait.until(EC.visibility_of_element_located((By.ID, 'display_select_input')))
        self.assertTrue(self.driver.find_element_by_class_name('select-workspace').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('display_select_input').is_displayed())


if __name__ == "__main__":
    import __main__
    output = run_test(TestLoginPage, data, __main__)
