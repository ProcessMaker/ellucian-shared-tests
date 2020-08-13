#!/usr/local/bin/python3
"""
Test 7: Two Elements

Prerequisites: URL, Username, Password
Testing: Functionality

Purpose

The purpose of this test is to verify there are two elements in dropdown menu after clicking “New” on Designer page.

Test Steps
Visit the URL
Login
Visit the Designer page
Click “New”
Verify there are two elements in dropdown menu
"""

import unittest
import json
from os import getenv
if getenv("ENVIRONMENT") == "local":
    from sys import path
    path.append('../includes')
    from __init__ import data

from test_parent import BaseTest
from util import run_test
from page import *


class TestDesignerNewDropDown(BaseTest):
    ''' Class to test Designer's New dropdown menu. '''

    def setUp(self):
        ''' Run before each test method. '''
        login_page = LoginPage(self.driver, data)
        login_page.go_to_page()
        login_page.login()
        self.assertionFailures = []

    def tearDown(self):
        ''' Run after each test method. '''
        self.assertEqual([], self.assertionFailures)

    def test_designer_new_project_dropdown(self):
        ''' Verify two elements in dropdown. '''

        new_process_page = DesignerPage(self.driver, data)

        try:
            self.assertTrue(new_process_page.new_project_has_two_options())
        except AssertionError as e:
            self.assertionFailures.append(str(e))


if __name__ == "__main__":
    import __main__
    output = run_test(TestDesignerNewDropDown, data, __main__)
