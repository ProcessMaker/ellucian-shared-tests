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
from api_requests import parse_response


class TestVariablesLoad(BaseTest):
    ''' Class to navigate to /oauth2/applications page to get client_id and client_secret,
    then make API calls to PM3 REST API. '''

    def test_variables_load(self):
        ''' Test that variables are in a JSON-parsable format. '''

        self.driver = login(data, self.driver, self.log)
        data_ = self.driver.data

        # Navigate to Oauth2 Applications page to get client id and client secret
        self.driver.get(data_['server_url'] + '/sys' + data_['server_workspace'] + '/en/neoclassic/oauth2/applications')
        self.wait.until(EC.visibility_of_element_located((By.ID, 'adminFrame')))
        self.driver.switch_to.frame(self.driver.find_element_by_id('adminFrame'))

        # Inspect Ellucian workflow
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'x-grid3-row')))
        self.driver.find_element_by_class_name('x-grid3-row').click()
        self.driver.find_element_by_id('ext-gen42').click()
        self.wait.until(EC.visibility_of_element_located((By.ID, 'ext-comp-1010')))

        # Get client id and client secret from window
        window_text = self.driver.find_element_by_id('ext-comp-1010').text
        client_id = re.search(r'(?<=ID:\s)\w+', window_text).group(0)
        client_secret = re.search(r'(?<=Secret:\s)\w+', window_text).group(0)
        self.driver.api = {
            'url': self.driver.data['server_url'],
            'workspace': self.driver.data['server_workspace']
        }
        auth = {
            'username': self.driver.data['username'],
            'password': self.driver.data['password'],
            'client_id': client_id,
            'client_secret': client_secret
        }

        # Verify variables list can be parsed as JSON
        response, self.driver = parse_response(self.driver, auth)
        self.assertTrue(response)

        self.log = self.driver.log


if __name__ == "__main__":
    import __main__
    output = run_test(TestVariablesLoad, data, __main__)
