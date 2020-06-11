#!/usr/local/bin/python3

import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_parent import BaseTest
from util import run_test


class TestAdminPage(BaseTest):
    ''' Class to run test that login fields exist. '''

    def test_admin_page(self):
        ''' Test that admin page displays. '''
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
        wait.until(EC.visibility_of_element_located((By.ID, 'SETUP')))
        
        # Click Admin link
        self.driver.find_element_by_id('SETUP').click()
        
        # Wait for Admin page to load
        wait.until(EC.visibility_of_element_located((By.ID, 'adminFrame')))
        
        # Verify that Admin page is loaded
        self.assertTrue(self.driver.find_element_by_id('adminFrame').is_displayed())        

if __name__ == "__main__":
    import __main__
    output = run_test(TestAdminPage, data, __main__)
