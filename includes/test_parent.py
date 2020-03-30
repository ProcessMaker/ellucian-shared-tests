#!/usr/local/bin/python3
"""
Defines BaseTest class
"""

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BaseTest(unittest.TestCase):
    """ The BaseTest class from which tests will inherit. """

    @classmethod
    def setUpClass(cls):
        ''' Set up browser instance. '''
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        cls.driver = webdriver.Chrome(options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        ''' End browser instance. '''
        cls.driver.close()
        cls.driver.quit()
