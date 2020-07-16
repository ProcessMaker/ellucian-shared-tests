#!/usr/local/bin/python3

""" Class for Oauth Page """

import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class OauthPage:
    ''' Contain Oauth Page methods and selectors. '''

    def __init__(self, driver, data):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 120)
        self.data = data
        self.page_url = self.data['server_url'] + '/sys' + self.data['server_workspace'] + '/en/neoclassic/oauth2/applications'

    def get_oauth_page(self):
        self.driver.log.append('Get Oauth Page')
        self.driver.get(self.page_url)
    
    def find_elements(self):
        self.driver.log.append('Get elements on Oauth Page')
        self.adminFrame = self.wait.until(EC.visibility_of_element_located((By.ID, 'adminFrame')))

    def switch_to_adminFrame(self):
        self.driver.log.append('Switch to adminFrame')
        self.driver.switch_to.frame(self.adminFrame)

    def find_elements_on_adminFrame(self):
        self.applications_table = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'x-grid3-row')))
        self.detail = self.wait.until(EC.visibility_of_element_located((By.ID, 'ext-gen42')))

    def get_adminFrame(self):
        self.driver.log.append('Switch to adminFrame')
        self.get_admin_page()
        self.find_elements()
        self.switch_to_adminFrame()
        self.find_elements_on_adminFrame()

    def find_elements_on_detail_window(self):
        self.detail_window = self.wait.until(EC.visibility_of_element_located((By.ID, 'ext-comp-1010')))

    def get_oauth_detail(self):
        self.get_adminFrame()
        self.applications_table.click()
        self.detail.click()
        self.find_elements_on_detail_window()
        return self.detail_window.text