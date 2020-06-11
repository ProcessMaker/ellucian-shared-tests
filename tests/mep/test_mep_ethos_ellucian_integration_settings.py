#!/usr/local/bin/python3

import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_parent import BaseTest
from util import run_test


class TestEthosIntegrationPlugin(BaseTest):
    ''' Test the Ellucian Ethos Integration Settings Panel. '''

    def test_ethos_integration_setup_panel(self):
        ''' Test that Ellucian Ethos Integration Settings Setup page displays. '''
        # Navigate to server
        self.driver.get(data['server_url'])
        
        # Select workspace and navigate to login page
        self.driver.find_element_by_id('display_select_input').click()
        self.driver.find_element_by_link_text(data['server_workspace']).click()
        self.driver.find_element_by_id('sentworkspace').click()

        # Wait for login page to load
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable((By.ID, 'form[BSUBMIT]')))
        
         # Enter user credentials and navigate to Processes page
        self.driver.find_element_by_id('form[USR_USERNAME]').send_keys(data['username'])
        self.driver.find_element_by_id('form[USR_PASSWORD_MASK]').send_keys(data['password'])
        self.driver.find_element_by_id('form[BSUBMIT]').click()
        
        # Wait for Processes page to load
        wait.until(EC.element_to_be_clickable((By.ID, 'SETUP')))
        
        # Click Admin link
        self.driver.find_element_by_id('SETUP').click()

        # Wait for Admin page to load
        wait.until(EC.visibility_of_element_located((By.ID, 'adminFrame')))
        
        # Locate and switch to Admin iframe
        self.driver.switch_to.frame(self.driver.find_element_by_id('adminFrame'))

        # Click Plugins link
        self.driver.find_element_by_id('west-panel__plugins').click()

        # Wait for Plugins page to load
        wait.until(EC.element_to_be_clickable((By.ID, 'extdd-54')))
        
        # Click Ellucian Ethos Integration Settings link
        self.driver.find_element_by_id('extdd-54').click()

        # Wait for Ellucian Ethos Integration Settings tab to load
        wait.until(EC.visibility_of_element_located((By.ID, 'setup-frame')))
        
        # Locate and switch to Setup iframe
        self.driver.switch_to.frame(self.driver.find_element_by_id('setup-frame'))
        
        # Wait for Setup tab to load
        wait.until(EC.element_to_be_clickable((By.ID, 'workspace-setup-tab')))

        ''' Assert page elements are displayed:
                New Workspace Setup tab
                Workspace Name
                Log Level
                Ellucian Ethos Integration Base URL
                Time Zone
                Ellucian Ethos Integration API Key
                Ellucian Ethos Integration API Key Visibility Icon (Masked)
                Cancel Button
                Save Button
        '''
        # New Workspace Setup tab
        self.assertTrue(self.driver.find_element_by_id('workspace-setup-tab').is_displayed())
        # Workspace Name
        self.assertTrue(self.driver.find_element_by_id('workspace-setup').is_displayed())
        # Log Level
        self.assertTrue(self.driver.find_element_by_name('PLUGIN_DEBUG_LEVEL').is_displayed())
        # Ellucian Ethos Integration Base URL
        self.assertTrue(self.driver.find_element_by_name('ETHOS_BASE_URL').is_displayed())
        # Time Zone
        self.assertTrue(self.driver.find_element_by_name('TIME_ZONE').is_displayed())
        # Ellucian Ethos Integration API Key + visibility icon (masked by default)
        self.assertTrue(self.driver.find_element_by_id('ethos_api_key').is_displayed())
        self.assertTrue(self.driver.find_element_by_id('toggle').is_displayed())
        self.assertTrue(self.driver.find_element_by_class_name('show').is_displayed())
        # Cancel button
        self.assertTrue(self.driver.find_element_by_id('cancel').is_displayed())
        # Save button
        self.assertTrue(self.driver.find_element_by_id('save').is_displayed())


if __name__ == "__main__":
    import __main__
    output = run_test(TestEthosIntegrationPlugin, data, __main__)
