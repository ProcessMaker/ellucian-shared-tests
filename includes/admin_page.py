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
        self.page_url = self.data['server_url'] + '/sys' + self.data['server_workspace'] + '/en/ellucianux/setup/main'

    def find_elements(self):
        self.driver.log.append('Find elements on Admin Page')
        self.adminFrame = self.wait.until(EC.visibility_of_element_located((By.ID, 'adminFrame')))

    def get_admin_page(self):
        self.driver.log.append('Get Admin page')
        self.driver.get(self.page_url)

    def switch_to_adminFrame(self):
        self.driver.log.append('Switch to adminFrame')
        self.driver.switch_to.frame(self.adminFrame)

    def switch_to_setup_frame(self):
        self.driver.log.append('Switch to setup_frame')
        self.driver.switch_to.frame(self.wait.until(EC.visibility_of_element_located((By.ID, 'setup-frame'))))

    def find_elements_on_adminFrame(self):
        self.driver.log.append('Find elements on adminFrame')
        self.plugins = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Plugins')))

    def get_adminFrame(self):
        self.get_admin_page()
        self.find_elements()
        self.switch_to_adminFrame()
        self.find_elements_on_adminFrame()
 
    ''' Settings panel
    '''

    def find_elements_on_settings_tab(self):
        self.driver.log.append('Find elements on Settings tab')
        self.case_list_cache_builder = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Case List Cache Builder')]")))
        self.system_information = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'System information')))

    def find_system_information_elements(self):
        self.driver.log.append('Find elements on System information panel')
        self.driver.get(self.data['server_url'] + '/sys' + self.data['server_workspace'] + '/en/ellucianux/setup/systemInfo?option=processInfo')
        from time import sleep
        sleep(2)
        self.process_information_table = self.wait.until(EC.visibility_of_element_located((By.ID, 'ext-gen13-gp-section-Process Information-bd'))).text
        self.system_information_table = self.wait.until(EC.visibility_of_element_located((By.ID, 'ext-gen13-gp-section-System information-bd'))).text

    def find_case_list_cache_builder_elements(self):
        self.driver.log.append('Find elements on Case List Cache Builder panel')
        self.driver.get(self.data['server_url'] + '/sys' + self.data['server_workspace'] + '/en/ellucianux/setup/appCacheViewConf')
        from time import sleep
        sleep(2)
        self.workflow_applications_cache_info = self.wait.until(EC.visibility_of_element_located((By.ID, 'ext-gen20'))).text

    def get_case_list_cache_builder(self):
        self.find_case_list_cache_builder_elements()
        return self.workflow_applications_cache_info
        
    def get_system_information(self):
        self.find_system_information_elements()
        return (self.process_information_table, self.system_information_table)

    ''' Plugins panel
    '''
    def find_elements_on_plugins_tab(self):
        self.plugins_manager = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Plugins Manager")))

    def find_elements_on_setup_frame(self):
        from time import sleep
        sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'x-grid3-row')))
        self.elements = self.driver.find_elements_by_class_name('x-grid3-row')

    def get_plugins(self):
        self.get_adminFrame()
        self.find_elements_on_adminFrame()
        self.plugins.click()
        self.find_elements_on_plugins_tab()
        self.plugins_manager.click()
        self.switch_to_setup_frame()
        self.find_elements_on_setup_frame()
        # Double check this line
        return [element.text for element in self.elements]
