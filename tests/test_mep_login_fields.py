#!/usr/local/bin/python3

from sys import path
path.append('../')

import unittest
from includes.test_parent import BaseTest
from includes.util import run_test


class TestLoginFields(BaseTest):
    ''' Class to run test that login fields exist. '''
    data = {}

    def test_login_elements(self):
        ''' Test that login elements exist on page. '''
        # Navigate to server
        self.driver.get(data['server_url'])
        
        # Select workspace and navigate to login page
        self.driver.find_element_by_id('display_select_input').click()
        self.driver.find_element_by_link_text(data['server_workspace']).click()
        self.driver.find_element_by_id('sentworkspace').click()
        
        # Verify that login fields are displayed
        self.assertTrue(self.driver.find_element_by_id('form[USR_USERNAME]').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('form[USR_PASSWORD_MASK]').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('form[BSUBMIT]').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('page-top').is_displayed())


if __name__ == "__main__":
    import __main__
    output = run_test(TestLoginFields, data, __main__)
