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

    def find_elements_on_adminFrame(self):
        self.case_list_cache_builder = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Case List Cache Builder')]")))
        self.setup_frame = self.wait.until(EC.visibility_of_element_located((By.ID, 'setup-frame')))

    def find_elements_on_setup_frame(self):
        self.table = self.wait.until(EC.visibility_of_element_located((By.ID, 'ext-gen12')))
    
    def get_admin_page(self):
        self.driver.get(self.page_url)

    def switch_to_adminFrame(self):
        self.driver.switch_to.frame(self.adminFrame)

    def switch_to_setup_frame(self):
        self.driver.switch_to.frame(self.setup_frame)

    def get_case_list_cache_builder(self):
        self.get_admin_page()
        self.switch_to_adminFrame()
        self.case_list_cache_builder.cick()
        self.switch_to_setup_frame()
        return self.table.text
        