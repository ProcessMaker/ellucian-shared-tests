#!/usr/local/bin/python3

""" Class for Processes Page """

import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ProcessesPage:
    ''' Contain Processes Page methods and selectors. '''

    def __init__(self, driver, data):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 120)
        self.data = data

    def get_processes_page(self):
        self.driver.get(self.data['server_url'])

    def is_processes_page(self):
        return (self.driver.current_url == self.data['server_url'] + '/sys' + self.data['server_workspace'] + '/en/ellucianux/processes/main')

    def is_loaded(self):
        self.driver.log.append('Waiting for main page to load')
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, 'SETUP')))
            self.wait.until(EC.visibility_of_element_located((By.ID, 'pm_main_table')))
            self.driver.log.append('Main page loaded successfully')
            return True
        except:
            self.driver.log.append('Main page failed to load')
            return False
            