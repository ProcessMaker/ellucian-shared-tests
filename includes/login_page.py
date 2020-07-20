#!/usr/local/bin/python3

""" Class for Login Page """

import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from api_requests import get_response_code


class LoginPage:
    ''' Contain Login Page methods and selectors. '''

    def __init__(self, driver, data):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 120)
        self.data = data
        self.login_page_url = self.data['server_url'] + '/sys/en/ellucianux/login/login'


    def find_elements(self):
        self.username_field = self.wait.until(EC.visibility_of_element_located((By.ID, 'form[USR_USERNAME]')))
        self.password_field = self.wait.until(EC.visibility_of_element_located((By.ID, 'form[USR_PASSWORD_MASK]')))
        self.workspace_dropdown = self.wait.until(EC.visibility_of_element_located((By.ID, 'form[USER_ENV]')))
        self.submit_button = self.wait.until(EC.visibility_of_element_located((By.ID, 'form[BSUBMIT]')))
    

    def get_login_page(self):
        self.driver.log.append(get_response_code(self.driver, self.data))
        self.driver.get(self.login_page_url)


    def login(self):
        self.get_login_page()
        self.find_elements()
        self.driver.log.append('Attempting login...')
        self.username_field.send_keys(self.data['username'])
        self.password_field.send_keys(self.data['password'])
        self.workspace_dropdown.send_keys(self.data['server_workspace'])
        self.submit_button.click()
        return self.driver

