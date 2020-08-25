#!/usr/local/bin/python3

"""
Test 9: Server Response Time
Testing: Functionality

The purpose of this test is to verify the Designer page loads in 5 seconds or less.

Test Steps
1.Visit the URL
2.Login
3.Vist the Designer page
7.Verify specified elements display in 5 seconds or less

"""

from os import getenv
if getenv("ENVIRONMENT") == 'local':
    from sys import path
    path.append('../includes')
    from __init__ import data

from test_parent import BaseTest
from util import run_test
from page import *

class TestDesignerPageResponseTime(BaseTest):
    ''' Test Designer page loads in 5 seconds or less. '''

    def setUp(self):
        ''' Run before each test method. '''

        login_page = LoginPage(self.driver, data)
        self.assertTrue(login_page.login())
        self.assertionFailures = []

    def tearDown(self):
        ''' Run after each test method. '''

        # Check for test failures added during execution
        self.assertEqual([], self.assertionFailures)

    def test_designer_page_loads_in_five_seconds(self):
        ''' Navigate to Designer page and verify elements display
            in five seconds. '''

        # Create Designer Page object
        designer_page = DesignerPage(self.driver, data)

        try:
            self.assertTrue(designer_page.is_loaded())
        except AssertionError as e:
            self.assertionFailures.append(str(e))


if __name__ == "__main__":
    import __main__
    output = run_test(TestDesignerPageResponseTime, data, __main__)
