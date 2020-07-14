#!/usr/local/bin/python3

import requests
import json
import re
import unittest
from test_parent import BaseTest
from util import run_test, login, regex
from api_requests import parse_response
from login_page import LoginPage
from oauth_page import OauthPage


class TestVariablesLoad(BaseTest):
    ''' Class to navigate to /oauth2/applications page to get client_id and client_secret,
    then make API calls to PM3 REST API. '''

    def test_variables_load(self):
        ''' Test that variables are in a JSON-parsable format. '''

        self.driver = LoginPage(self.driver, self.data).login()

        oauth_detail = OauthPage(self.driver, self.data).get_oauth_detail()

        client_id = regex("r'(?<=ID:\s)\w+'", oauth_detail)
        client_secret = regex("r'(?<=Secret:\s)\w+'", oauth_detail)

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
        self.assertTrue(response)


if __name__ == "__main__":
    import __main__
    output = run_test(TestVariablesLoad, data, __main__)
