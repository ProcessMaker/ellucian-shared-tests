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

    def test_login(self):
        ''' Test that landing page loads. '''

        # Navigate to login page and log in
        login_page = LoginPage(self.driver, data)
        login_page.go_to_page()
        login_page.login()

        # Verify Designer page loads
        designer_page = DesignerPage(self.driver, data)
        self.assertTrue(designer_page.is_loaded())


if __name__ == "__main__":
    import __main__
    output = run_test(TestLoginPage, data, __main__)
