#!/usr/local/bin/python3

"""
Test 10: Trigger Wizard
Testing: Functionality

The purpose of this test is to verify there are no more than three
Trigger Wizards present in workflow Triggers.

Test Steps
1.Visit the URL
2.Login
3.Vist the Designer page
4.Double click on workflow
5.Double click on Triggers
6.Click on +Wizard
7.Verify only three triggers display

"""

from os import getenv
if getenv("ENVIRONMENT") == 'local':
    from sys import path
    path.append('../includes')
    from __init__ import data

from test_parent import BaseTest
from util import run_test
from page import *

class TestTriggerWizardListLength(BaseTest):
    ''' Test only three triggers display under +Wizard button. '''

    def setUp(self):
        ''' Run before each test method. '''

        login_page = LoginPage(self.driver, data)
        self.assertTrue(login_page.login())
        self.assertionFailures = []

    def tearDown(self):
        ''' Run after each test method. '''

        # Check for test failures added during execution
        self.assertEqual([], self.assertionFailures)

    def test_only_three_triggers_display_under_trigger_wizard(self):
        ''' Navigate to workflow Triggers, click +Wizard and
            verify only three triggers display. '''

        # Create Designer Page object
        designer_page = DesignerPage(self.driver, data)

        # Double click on Dynaform Styling workflow
        designer_page.open_workflow()
            # method on Designer page to search for a workflow containing text ("Dynaform Styling"
            # in this case), then double click it

        # Wait for edit workflow to load
        designer_page.open_workflow_triggers()
            # Use same double click method to double click on Triggers

        designer_page.click_plus_wizard()
            # Find row element containing Amount
            # Click on Edit for this row

        triggers = designer_page.count_triggers()
        # Count number of triggers available

        # Wait for preview to load

        try:
            self.assertEqual(triggers, 3)
            self.driver.log.append('Correct number of triggers available for selection')
        except AssertionError as e:
            self.driver.log.append('Incorrect number of triggers: ' + str(triggers) )
            self.assertionFailures.append(str(e))


if __name__ == "__main__":
    import __main__
    output = run_test(TestTriggerWizardListLength, data, __main__)
    
