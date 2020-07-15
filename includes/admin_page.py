#!/usr/local/bin/python3

""" Class for Admin Page """

import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:
    ''' Contain Login Page methods and selectors. '''

    def __init__(self, driver, data):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 120)
        self.data = data
        self.page_url = self.data['server_url'] + '/sys' + data['server_workspace'] + '/en/ellucianux/setup/main'

    def find_elements(self):
        self.adminFrame = self.wait.until(EC.visibility_of_element_located((By.ID, 'adminFrame')))

    def get_admin_page(self):
        self.driver.get(self.page_url)

    def switch_to_adminFrame(self):
        self.driver.switch_to.frame(self.adminFrame)

    def switch_to_setup_frame(self):
        self.driver.switch_to.frame(self.wait.until(EC.visibility_of_element_located((By.ID, 'setup-frame'))))

    def get_adminFrame(self):
        self.get_admin_page()
        self.find_elements()
        self.switch_to_adminFrame()
        self.find_elements_on_adminFrame()

    def find_elements_on_adminFrame(self):
        self.plugins = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Plugins')))
 
    ''' Settings panel
    '''

    def find_elements_on_settings_tab(self):
        self.case_list_cache_builder = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Case List Cache Builder')]")))
        self.system_information = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'System information')))

    def find_system_information_elements(self):
        self.process_information_table = self.wait.until(EC.visibility_of_element_located((By.ID, 'ext-gen13-gp-section-Process Information-bd')))
        self.system_information_table = self.wait.until(EC.visibility_of_element_located((By.ID, 'ext-gen13-gp-section-System information-bd')))

    def find_case_list_cache_builder_elements(self):
        self.workflow_applications_cache_info = self.wait.until(EC.visibility_of_element_located((By.ID, 'ext-gen12')))

    def get_case_list_cache_builder(self):
        self.get_adminFrame()
        self.find_elements_on_settings_tab()
        self.case_list_cache_builder.click()
        self.switch_to_setup_frame()
        self.find_case_list_cache_builder_elements()
        return self.workflow_applications_cache_info.text
        
    def get_system_information(self):
        self.get_adminFrame()
        self.system_information.click()
        self.switch_to_setup_frame()
        self.find_system_information_elements()
        return (self.process_information_table.text, self.system_information_table.text)

    ''' Plugins panel
    '''
    def find_elements_on_plugins_tab(self):
        self.plugins_manager = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Plugins Manager")))

    def get_plugins(self):
        self.get_adminFrame()
        self.find_elements_on_adminFrame()
        self.plugins.click()
        self.plugins_manager.click()
        self.switch_to_setup_frame()
        # Double check this line
        return [element.text for element in self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'x-grid3-row')))]
