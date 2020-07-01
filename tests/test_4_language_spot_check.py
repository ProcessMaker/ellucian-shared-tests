#!/usr/local/bin/python3

import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_parent import BaseTest
from util import run_test, login, read_from_json_file
import re
import json


class TestLanguageSpotCheck(BaseTest):
    ''' Class to run test that checks for untranslated values. '''

    def test_language_spot_check(self):
        ''' Test that there are no visible labels. '''
        # Login using configured url, workspace, username, and password
        self.driver = login(data, self.driver, self.log)
        
        # Wait for Processes page to load
        self.wait.until(EC.visibility_of_element_located((By.ID, 'SETUP')))

        languages = read_from_json_file(self.driver.data['repository_path'],
                                                '/includes/expected_values.json', 'Languages')
        
        # Get current URL and re-get URL with different language
        for i in range(1, len(languages)):
            url = self.driver.current_url
            url = re.sub('/' + languages[i - 1] + '/', '/' + languages[i] + '/', url)
            self.driver.get(url)
            
            # Wait for Processes page to load
            self.wait.until(EC.visibility_of_element_located((By.ID, 'SETUP')))

            # Assert that labels are not present on page
            self.assertEqual(None, re.search(r'\*\*(\w+)\*\*', self.driver.page_source))

        self.driver.log.append('Test passed')
        self.log = self.driver.log


if __name__ == "__main__":
    import __main__
    data['repository_path'] = repository_path
    output = run_test(TestLanguageSpotCheck, data, __main__)
