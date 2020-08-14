#!/usr/local/bin/python3
""" Module to contain helper functions that cut down on redundant code in main calls.
"""

import unittest
import re
import json
from contextlib import redirect_stdout
from io import StringIO
import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_classes import CustomTextTestRunner, CustomTestLoader
from api_requests import get_response_code


def run_test(classname, data, modulename):
    ''' Function to run test and redirect output from stdout
        and return results in PM4 output variable.
    '''
    if data is {}:
        return 'data dictionary must not be empty'

    if not classname:
        return 'classname missing'

    if not data:
        return 'data missing'

    if not modulename:
        return 'modulename missing'

    suite = CustomTestLoader().loadTestsFromModule(modulename)
    classname.data = data
    with StringIO() as buffer:
        with redirect_stdout(buffer):
            log = CustomTextTestRunner(stream=buffer).run(suite).log
            if 'ERROR' in log[-1]:
                log[-1] = parse_log_error(log[-1])
            elif 'WARNING' in log[-1]:
                log[-1] = parse_log_warning(log[-1])
            test_output = buffer.getvalue()
            return {"result": parse_results(test_output), "message": log}

def parse_log_error(log_message):
    ''' Function to capture ERROR message.
    '''
    return 'ERROR: ' + re.search(r'(?<=ERROR<\/strong>:\s)([^<]+)', log_message).group(0)


def parse_log_warning(log_message):
    ''' Function to capture WARNING message.
    '''
    return 'WARNING: ' + re.search(r'(?<=WARNING<\/strong>:\s)([^<]+)', log_message).group(0)


def parse_results(buffer):
    ''' Function to parse the unittest results into PM4-friendly format.
    '''
    if not buffer or buffer is '':
        return 'No unittest result detected'

    if buffer.startswith('.'):
        return 'SUCCESS'
    elif buffer.startswith('F') or buffer.startswith('E'):
        return 'FAIL'
    # else:
    #    return 'ERROR'


def timezone_check(driver):
    ''' Function to check for time zone config page and bypass it.
    '''
    try:
        driver.find_element_by_id('form[USR_USERNAME]')
        driver.log.append('Unknown login failure')
        from time import sleep
        sleep(3)
        source = driver.page_source
        if 'ERROR' in source or 'WARNING' in source:
            driver.log.append(source)
    except:
        pass

    wait = WebDriverWait(driver, 30)

    # Wait for page to load
    wait.until(EC.visibility_of_element_located((By.ID, 'pm_main_table')))
    driver.log.append('Login succeeded')
    driver.log.append('Checking for timezone reset')

    try:
        driver.find_element_by_id('form[BROWSER_TIME_ZONE]')
        driver.find_element_by_id('form[BTNOK]').click()
        driver.log.append('Reset timezone')
    except selenium.common.exceptions.NoSuchElementException:
        driver.log.append('Timezone not reset')

def read_from_json_file(repository_path, filename, key=''):
    ''' Function to open JSON file, read, and deserialize.
    Return the entire dictionary or specific key.
    '''
    with open(repository_path + filename) as jsonFile:
        expected_values = json.loads(jsonFile.read())
        if key:
            return expected_values[0][key]
        return expected_values[0]
