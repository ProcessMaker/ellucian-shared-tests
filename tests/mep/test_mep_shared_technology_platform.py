#!/usr/local/bin/python3

import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_parent import BaseTest
from util import run_test


class TestSharedTechnologyPlatform(BaseTest):
    ''' Test the Ellucian Ethos Integration Shared Technology Panel. '''

    def test_ethos_integration_setup_panel(self):
        ''' Test that Ellucian Ethos Integration Settings Shared Technology Platform page displays. '''
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
        wait.until(EC.element_to_be_clickable((By.ID, 'stp-tab')))

        # Click Shared Technology Platform link
        self.driver.find_element_by_id('stp-tab').click()

        # Wait for Shared Technology Platform tab to load
        wait.until(EC.visibility_of_element_located((By.ID, 'stp')))

        ''' Assert page elements are displayed:
                'Select at least one shared source' Text
                Shared Integration Dropdown
                Shared Student Dropdown
                Add STP Code(s)
                Add STP Code Button
                STP Code Table
                STP Code
                Display Name
                Source Applications
                API Key
                Actions
                Visibility Icon
                Edit Icon
                Delete Icon
                Integrate Ethos data only through STP Checkbox
                Cancel Button
                Save Button
        '''
        # 'Select at least one shared source' Text
        self.assertTrue('Select at least one shared source' in self.driver.page_source)
        # Shared Integration Dropdown
        self.assertTrue(self.driver.find_elements_by_class_name('control-label') != 0)
        self.assertTrue(self.driver.find_element_by_id('SHARED_INTEGRATION').is_displayed())
        # Shared Student Dropdown
        self.assertTrue(self.driver.find_element_by_id('SHARED_STUDENT').is_displayed())
        # Add STP Code(s)
        self.assertTrue('Add STP code(s)*' in self.driver.page_source)
        # Add STP Code Button
        self.assertTrue(self.driver.find_element_by_id('add-stp-code').is_displayed())
        # STP Code Table
        self.assertTrue(self.driver.find_element_by_id('mep_settings_table').is_displayed())

        ''' Current issues:
                - Cannot delete current STP codes because of dependencies
                  (therefore cannot view table when it's empty)
                - Cannot add new STP codes
                  - STP code* dropdown list is empty
                  - Banner Integration dropdown is greyed out
                  - Banner Student dropdown is greyed out
                - Cannot view Shared Integration and Shared Student dropdowns
        # STP Code
        # Display Name
        # Source Applications
        # API Key
        # Actions
        # Visibility Icon
        # Edit Icon
        # Delete Icon
        '''

        # Integrate Ethos data only through STP Checkbox
        self.assertTrue(self.driver.find_element_by_id('DISABLE_NON_MEP').is_displayed())
        # Cancel Button
        self.assertTrue(self.driver.find_element_by_id('cancel-stp').is_displayed())
        # Save Button
        self.assertTrue(self.driver.find_element_by_id('save-stp').is_displayed())


if __name__ == "__main__":
    import __main__
    output = run_test(TestSharedTechnologyPlatform, data, __main__)
