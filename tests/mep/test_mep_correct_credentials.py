#!/usr/local/bin/python3

import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_parent import BaseTest
from util import run_test


class TestCorrectCredentials(BaseTest):
    ''' Class to run test that correct login credentials work. '''

    def test_correct_credentials(self):
        ''' Test that correct credentials work. '''
        # Navigate to server
        self.driver.get(data['server_url'])
        
        # Select workspace and navigate to login page
        self.driver.find_element_by_id('display_select_input').click()
        self.driver.find_element_by_link_text(data['server_workspace']).click()
        self.driver.find_element_by_id('sentworkspace').click()

        # Wait for login page to load
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.ID, 'form[BSUBMIT]')))
        
        # Enter user credentials and navigate to Processes page
        self.driver.find_element_by_id('form[USR_USERNAME]').send_keys(data['username'])
        self.driver.find_element_by_id('form[USR_PASSWORD_MASK]').send_keys(data['password'])
        self.driver.find_element_by_id('form[BSUBMIT]').click()
        
        # Wait for Processes page to load
        wait.until(EC.element_to_be_clickable((By.ID, 'SETUP')))
        
        # Verify that Processes page is displayed
        self.assertEqual(self.driver.title, "(admin in mep)")


if __name__ == "__main__":
    import __main__
    output = run_test(TestCorrectCredentials, data, __main__)
