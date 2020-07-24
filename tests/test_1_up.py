#!/usr/loca/bin/python3

import unittest
from test_parent import BaseTest
from util import run_test
from login_page import LoginPage
from processes_page import ProcessesPage


class TestLoginPage(BaseTest):
    ''' Class to run test that page loads after login. '''

    def test_login(self):
        ''' Test that landing page loads. '''

        self.driver = LoginPage(self.driver, self.data).login()

        self.assertTrue(ProcessesPage(self.driver, self.data).is_loaded())


if __name__ == "__main__":
    import __main__
    output = run_test(TestLoginPage, data, __main__)
