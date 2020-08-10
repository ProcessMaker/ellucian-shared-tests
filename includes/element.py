#!/usr/local/bin/python3

from selenium.webdriver.support.ui import WebDriverWait

""" BasePageElement classes.
    Descriptors for getting and setting single elements.
    Available field locator types:
        ID,
        NAME,
        XPATH
    Extend a BasePageElement object:
        class TextFieldElement(BasePageElement)
    Instantiate extended object (inside of a Page class) with XPATH type:
        text_field = TextFieldElement('XPATH')
    Assign value to instantiated text_field:
        Page.text_field = "value"
    Retrieve value from instantiated text_field:
        Page.text_field
"""

class BasePageElement(object):
    """ Base Page Element class that's initialized on every Page Object class. """
    def __init__(self, element_type=None):
        ''' Initialize the BasePageElement object with its correct locator type. '''
        self.element_type = element_type

    def __set__(self, obj, value):
        ''' Set the text to the value element. '''
        driver = obj.driver

        # Set text to element found by id
        if self.element_type == 'ID':
            WebDriverWait(driver, 30).until(
                lambda driver: driver.find_element_by_id(self.locator)
            )
            driver.find_element_by_id(self.locator).clear()
            driver.find_element_by_id(self.locator).send_keys(value)

        # Set text to element found by name
        elif self.element_type == 'NAME':
            WebDriverWait(driver, 30).until(
                lambda driver: driver.find_element_by_name(self.locator)
            )
            driver.find_element_by_name(self.locator).clear()
            driver.find_element_by_name(self.locator).send_keys(value)

        # Set text to element found by xpath
        elif self.element_type == 'XPATH':
            WebDriverWait(driver, 30).until(
                lambda driver: driver.find_element_by_xpath(self.locator)
            )
            driver.find_element_by_xpath(self.locator).clear()
            driver.find_element_by_xpath(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        ''' Get the text of specified element. '''
        driver = obj.driver

        # Get text of element found by id
        if self.element_type == 'ID':
            WebDriverWait(driver, 30).until(
                lambda driver: driver.find_element_by_id(self.locator)
            )
            element = driver.find_element_by_id(self.locator)

        # Get text of element found by name
        elif self.element_type == 'NAME':
            WebDriverWait(driver, 30).until(
                lambda driver: driver.find_element_by_name(self.locator)
            )
            element = driver.find_element_by_name(self.locator)

        # Get text of element found by xpath
        elif self.element_type == 'XPATH':
            WebDriverWait(driver, 30).until(
                lambda driver: driver.find_element_by_xpath(self.locator)
            )
            element = driver.find_element_by_xpath(self.locator)
        return element.get_attribute("value")
