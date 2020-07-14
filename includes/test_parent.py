#!/usr/local/bin/python3
"""
Defines BaseTest class
"""

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

class BaseTest(unittest.TestCase):
    """ The BaseTest class from which tests will inherit. """
    page = ''
    log = ['Log created']

    @classmethod
    def setUpClass(cls):
        ''' Set up browser instance. '''
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        cls.driver = webdriver.Chrome(options=chrome_options)

        # Global driver wait variable
        cls.wait = WebDriverWait(cls.driver, 30)

        # Assign log to driver
        cls.driver.log = BaseTest.log

    @classmethod
    def tearDownClass(cls):
        ''' End browser instance. '''
        # Reassign log to class attribute
        BaseTest.log = cls.driver.log

        cls.driver.close()
        cls.driver.quit()
