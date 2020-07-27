#!/usr/local/bin/python3

""" Class for Designer Page """

import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class DesignerPage:
    ''' Contain Login Page methods and selectors. '''

    def __init__(self, driver, data):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.data = data
        self.page_url = self.data['server_url'] + '/sys' + self.data['server_workspace'] + '/en/ellucianux/processes/main'

    def is_designer_page(self):
        ''' Method to navigate to Designer page if not already at Designer page. '''
        if self.driver.current_url != self.page_url:
            self.driver.get(self.page_url)

    def get_page_elements(self):
        ''' Method to find elements on Designer page. '''
        self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, 'frameMain')))
        self.new_button = self.wait.until(EC.visibility_of_element_located((By.ID, 'ext-gen35')))

    def get_dropdown_elements(self):
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'x-menu-list-item')))
        self.dropdown_elements = self.driver.find_elements_by_class_name('x-menu-list-item')

    def new_project_has_two_elements(self):
        ''' Method to verify that New dropdown menu contains two elements. '''
        self.is_designer_page()
        self.get_page_elements()
        self.new_button.click()
        self.get_dropdown_elements()
        if len(self.dropdown_elements) == 2:
            return True
        return False


