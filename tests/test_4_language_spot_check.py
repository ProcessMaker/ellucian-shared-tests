#!/usr/local/bin/python3

import unittest
from test_parent import BaseTest
from util import run_test, read_from_json_file
import re
import json
from page import *


class TestLanguageSpotCheck(BaseTest):
    ''' Class to run test that checks for untranslated values. '''

    def setUp(self):
        ''' Run before each test method. '''
        login_page = LoginPage(self.driver, data)
        login_page.go_to_page()
        login_page.login()
        self.assertionFailures = []

    def tearDown(self):
        ''' Run after each test method. '''
        self.assertEqual([], self.assertionFailures)

    def test_language_spot_check(self):
        ''' Test that there are no visible labels. '''

        # Verify page has loaded
        landing_page = DesignerPage(self.driver, self.data).is_loaded()

        languages = read_from_json_file(data['repository_path'],
                                        '/includes/expected_values.json', 'Languages')

        # Get current URL and re-get URL with different language
        for i in range(1, len(languages)):
            url = re.sub('/' + languages[i - 1] + '/', '/' + languages[i] + '/',
                         landing_page.driver.current_url)

            landing_page.go_to_page(url)

            # Verify page has loaded
            landing_page.is_loaded()

            labels = re.search(r'\*\*(\w+)\*\*', self.driver.page_source)

            # Assert that labels are not present on page
            try:
                self.assertEqual(None, labels)
                self.driver.log.append('Successfully translated')
            except AssertionError as e:
                self.driver.log.append('Unsuccessful translation - Labels found')
                self.assertionFailures.append(str(e))


if __name__ == "__main__":
    import __main__
    data['repository_path'] = repository_path
    output = run_test(TestLanguageSpotCheck, data, __main__)
