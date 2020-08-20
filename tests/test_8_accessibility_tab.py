#!/usr/local/bin/python3
"""
Test 8: Accessibility Tab
Testing: Functionality

Purpose

The purpose of this test is to verify that skin is updated. (Accessibility fix is a part of that skin update.)

Test Steps
1.Visit URL
2.Login
3.Visit the Designer page
4.Open Dynaform Styling workflow
5.Double click Dynaforms
6.Click Edit Amount
7.Click preview
8.Verify that every element can be tabbed through

"""

from test_parent import BaseTest
from util import run_test
from page import *


class TestAccessibilityTabs(BaseTest):
    ''' Test elements can be tabbed through in Dynaform Styling workflow preview. '''

    def setUp(self):
        ''' Run before each test method. '''

        # Keep track of test failures without pausing tests midway
        self.assertionFailures = []

        # Log in to the server and check for 40x & 50x response codes
        login_page = LoginPage(self.driver, data)
        # Fail test immediately if login fails
        self.assertTrue(login_page.login())

    def tearDown(self):
        ''' Run after each test method. '''

        # Check for test failures added during execution
        self.assertEqual([], self.assertionFailures)

    def test_dynaform_styling_elements_can_be_tabbed_through(self):
        ''' Navigate to preview of Dynaform Styling workflow and tab through elements. '''


''' Main call. Used in every test file.
'''
if __name__ == "__main__":
    import __main__
    data['repository_path'] = repository_path
    output = run_test(TestLoginPage, data, __main__)
