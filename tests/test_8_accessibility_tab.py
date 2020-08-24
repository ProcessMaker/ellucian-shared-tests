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
from os import getenv
if getenv("ENVIRONMENT") == 'local':
    from sys import path
    path.append('../includes')
    from __init__ import data

from test_parent import BaseTest
from util import run_test
from page import *


class TestAccessibilityTabs(BaseTest):
    ''' Test elements can be tabbed through in Dynaform Styling workflow preview. '''

    def setUp(self):
        ''' Run before each test method. '''

        login_page = LoginPage(self.driver, data)
        self.assertTrue(login_page.login())
        self.assertionFailures = []

    def tearDown(self):
        ''' Run after each test method. '''

        # Check for test failures added during execution
        self.assertEqual([], self.assertionFailures)

    def test_dynaform_styling_elements_can_be_tabbed_through(self):
        ''' Navigate to preview of Dynaform Styling workflow and tab through elements. '''

        # Create Designer Page object
        designer_page = DesignerPage(self.driver, data)

        # Double click on Dynaform Styling workflow
        designer_page.open_workflow()
            # method on Designer page to search for a workflow containing text ("Dynaform Styling"
            # in this case), then double click it

        # Wait for edit workflow to load
        designer_page.open_workflow_dynaforms()
            # Use same double click method to double click on Dynaforms

        # Wait for window to load
        designer_page.edit_row()
            # Find row element containing Amount
            # Click on Edit for this row

        designer_page.click_preview()
        # Click on Preview button

        # Wait for preview to load

        try:
            self.assertEqual(designer_page.interactable_elements_are_tab_accessible(23), 'Button_1')
            self.driver.log.append('Successful accessibility check')
        except AssertionError as e:
            self.driver.log.append('Preview could not be tabbed through')
            self.assertionFailures.append(str(e))


if __name__ == "__main__":
    import __main__
    output = run_test(TestAccessibilityTabs, data, __main__)
    
