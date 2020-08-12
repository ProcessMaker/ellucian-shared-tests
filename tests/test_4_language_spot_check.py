#!/usr/local/bin/python3

import unittest
from test_parent import BaseTest
from util import run_test, read_from_json_file
import re
import json
from login_page import LoginPage
from processes_page import ProcessesPage


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

        ProcessesPage(self.driver, self.data).is_loaded()

        languages = read_from_json_file(data['repository_path'],
                                        '/includes/expected_values.json', 'Languages')

        # Get current URL and re-get URL with different language
        for i in range(1, len(languages)):
            url = re.sub('/' + languages[i - 1] + '/', '/' + languages[i] + '/', self.driver.current_url)

            self.driver.get(url)

            ProcessesPage(self.driver, self.data).is_loaded()

            labels = re.search(r'\*\*(\w+)\*\*', self.driver.page_source)

            # Assert that labels are not present on page
            try:
                self.assertEqual(None, labels)
                self.driver.log.append('Labels not found')
            except:
                self.driver.log.append('Labels found')
                self.fail()


if __name__ == "__main__":
    import __main__
    data['repository_path'] = repository_path
    output = run_test(TestLanguageSpotCheck, data, __main__)
