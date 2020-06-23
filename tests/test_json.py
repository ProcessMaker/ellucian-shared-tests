#!/usr/local/bin/python3

import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_parent import BaseTest
from util import run_test, login


class TestImport(BaseTest):
    ''' Class to import file. '''

    def test_json_import(self):
        ''' Test that file can be imported. '''
        # Login using configured url, workspace, username, and password
        self.driver = login(data, self.driver)
        
        # Wait for Processes page to load
        self.wait.until(EC.visibility_of_element_located((By.ID, 'SETUP')))
        
        # Open json file
        with open(repository_path + '/includes/expected_values.json') as json_file:
            json_file.read()
            
        # Verify that Processes page elements have loaded
        self.assertTrue(self.driver.find_element_by_id('pm_main_table'))
        self.assertTrue(self.driver.find_element_by_id('pm_header'))
        self.assertTrue(self.driver.find_element_by_class_name('Footer'))


if __name__ == "__main__":
    import __main__
    data.repository_path = repository_path
    output = run_test(TestImport, data, __main__)
