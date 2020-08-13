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

    def test_designer_new_project_dropdown(self):
        ''' Verify two elements in dropdown. '''
        self.driver = LoginPage(self.driver, data).login()

        self.assertTrue(DesignerPage(self.driver, data).new_project_has_two_elements())


if __name__ == "__main__":
    import __main__
    output = run_test(TestDesignerNewDropDown, data, __main__)
