#!/usr/local/bin/python3

import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_parent import BaseTest
from util import run_test, login
import re


class TestLanguageSpotCheck(BaseTest):
    ''' Class to run test that checks for untranslated values. '''

    def test_language_spot_check(self):
        ''' Test that there are no visible labels. '''
        # Login using configured url, workspace, username, and password
        self.driver = login(data, self.driver)
        
        # Wait for Processes page to load
        self.wait.until(EC.visibility_of_element_located((By.ID, 'SETUP')))
        
        # Get current URL and re-get URL with different language
        langs = self.driver.data['language']
        for i in range(1, len(langs)):
            url = self.driver.current_url
            url = re.sub('/' + langs[i - 1] + '/', '/' + langs[i] + '/', url)
            self.driver.get(url)

            # Wait for Processes page to load
            self.wait.until(EC.visibility_of_element_located((By.ID, 'SETUP')))

            # Assert that labels are not present on page
            self.assertEqual(None, re.search(r'\*\*(\w+)\*\*', self.driver.page_source))


if __name__ == "__main__":
    import __main__
    data['language'] = ['en', 'es', 'fr']
    output = run_test(TestLanguageSpotCheck, data, __main__)
