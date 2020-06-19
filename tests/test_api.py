#!/usr/local/bin/python3

import requests
import json
import re
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from test_parent import BaseTest
from util import run_test, login


class TestVariablesLoad(BaseTest):
    ''' Class to navigate to /oauth2/applications page to get client_id and client_secret,
    then make API calls to PM3 REST API. '''

    def test_variables_load(self):
        ''' Test that variables are in a JSON-parsable format. '''
        # Login using configured url, workspace, username, and password
        self.driver = login(data, self.driver)
        data_ = self.driver.data

        # Navigate to Oauth2 Applications page to get client id and client secret
        self.driver.get(data_['server_url'] + '/sys' + data_['server_workspace'] + '/en/neoclassic/oauth2/applications')
        self.wait.until(EC.visibility_of_element_located((By.ID, 'adminFrame')))
        self.driver.switch_to.frame(self.driver.find_element_by_id('adminFrame'))

        # Inspect Ellucian workflow and get client id and client secret
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'x-grid3-row')))
        self.driver.find_element_by_class_name('x-grid3-row').click()
        self.driver.find_element_by_id('ext-gen42').click()
        self.wait.until(EC.visibility_of_element_located((By.ID, 'ext-comp-1010')))
        window_text = self.driver.find_element_by_id('ext-comp-1010').text
        client_id = re.search(r'(?<=ID:\s)\w+', window_text).group(0)
        client_secret = re.search(r'(?<=Secret:\s)\w+', window_text).group(0)
        auth = {
            'username': self.driver.data['username'],
            'password': self.driver.data['password'],
            'client_id': client_id,
            'client_secret': client_secret
        }

        # Verify variables list can be parsed as JSON
        self.assertTrue(self.parse_response(auth))


    def parse_response(self, auth):
        ''' Method to verify variable list can be parsed as JSON. '''
        try:
            json.loads(self.get_variable_list(auth))
            return True
        except json.decoder.JSONDecodeError:
            return False

    def get_variable_list(self, auth):
        ''' Method to get variable list using project id. '''
        project_id, token = self.get_project_id(auth)
        response = requests.get('https://mep.dev-ellucian-us.processmaker.com/api/1.0/mep/project/' + project_id + '/process-variables', headers=token)
        return response.text

    def get_project_id(self, auth):
        ''' Method to get project id of first process in process list. '''
        token = {"Authorization": 'Bearer ' + self.get_access_token(auth)}
        response = requests.get('https://mep.dev-ellucian-us.processmaker.com/api/1.0/mep/project', headers=token)
        return (json.loads(response.text)[0]['prj_uid'], token)

    ''' Once requests module is installed into Docker container, move this method to util.py. '''
    def get_access_token(self, auth):
        ''' Method to grab access token through password grant. '''
        payload = [
            ("grant_type", "password"),
            ("scope", "*"),
            ("client_id", auth['client_id']),
            ("client_secret", auth['client_secret']),
            ("username", auth['username']),
            ("password", auth['password'])
            ]
        response = requests.post('https://mep.dev-ellucian-us.processmaker.com/mep/oauth2/token', data=payload)
        text = json.loads(response.text)
        return text['access_token']


if __name__ == "__main__":
    import __main__
    output = run_test(TestVariablesLoad, data, __main__)
