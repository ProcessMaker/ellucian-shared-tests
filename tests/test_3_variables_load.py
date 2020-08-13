#!/usr/local/bin/python3

import requests
import json
import re
import unittest
from test_parent import BaseTest
from util import run_test
from api_requests import parse_response
from page import *


class TestVariablesLoad(BaseTest):
    ''' Class to navigate to /oauth2/applications page to get client_id and client_secret,
    then make API calls to PM3 REST API. '''

    def setUp(self):
        ''' Run before each test method. '''
        login_page = LoginPage(self.driver, data)
        login_page.login()
        self.assertionFailures = []

    def tearDown(self):
        ''' Run after each test method. '''
        self.assertEqual([], self.assertionFailures)

    def test_variables_load(self):
        ''' Test that variables are in a JSON-parsable format. '''

        oauth_creds = AdminPage(self.driver, self.data).get_oauth_credentials()

        client_id = re.search(r'(?<=ID:\s)\w+', oauth_creds).group(0)
        client_secret = re.search(r'(?<=Secret:\s)\w+', oauth_creds).group(0)

        self.driver.api = {
            'url': data['server_url'],
            'workspace': data['server_workspace']
        }
        auth = {
            'username': data['username'],
            'password': data['password'],
            'client_id': client_id,
            'client_secret': client_secret
        }

        # Verify variables list can be parsed as JSON
        response, self.driver = parse_response(self.driver, auth)
        try:
            self.assertTrue(response)
            self.driver.log.append('Valid JSON response')
        except AssertionError as e:
            self.driver.log.append('Corrupted JSON. Variable list will not load')
            self.assertionFailures.append(str(e))


if __name__ == "__main__":
    import __main__
    output = run_test(TestVariablesLoad, data, __main__)
