#!/usr/local/bin/python3

from os import getenv
if getenv("ENVIRONMENT") == 'local':
    from sys import path
    path.append('../includes')
    from __init__ import data

from test_parent import BaseTest
from util import run_test
from page import *


class TestLoginPage(BaseTest):
    ''' Class to run test that page loads after login. '''
    def setUp(self):
        ''' Run before each test method. '''
        self.assertionFailures = []

    def tearDown(self):
        ''' Run after each test method. '''
        self.assertEqual([], self.assertionFailures)

    def test_login(self):
        ''' Test that landing page loads. '''

        # Navigate to login page and log in
        login_page = LoginPage(self.driver, data)
        login_page.login()

        # Verify Designer page loads
        designer_page = DesignerPage(self.driver, data)
        try:
            self.assertTrue(designer_page.is_loaded())
            self.log.append('Login succeeded')
        except AssertionError as e:
            self.log.append('Login failed')
            self.assertionFailures.append(str(e))


if __name__ == "__main__":
    import __main__
    output = run_test(TestLoginPage, data, __main__)
