#!/usr/local/bin/python3

import json
import requests


def parse_response(driver, auth):
    ''' Method to verify variable list can be parsed as JSON. '''
    try:
        variable_list, driver = get_variable_list(driver, auth)
        json.loads(variable_list)
        driver.log.append('Variable list loaded')
        return True, driver
    except json.decoder.JSONDecodeError:
        driver.log.append('JSON Decode Error. First 20 chars of response: ' + variable_list[:20])
        return False, driver


def get_variable_list(driver, auth):
    ''' Method to get variable list using project id. '''
    ret = get_project_id(driver, auth)
    project_id = ret[0]
    token = ret[1]
    driver = ret[2]
    response = requests.get(driver.api['url'] + '/api/1.0/' + driver.api['workspace'] + '/project/' + project_id + '/process-variables', headers=token)
    driver.log.append('Acquired variable list')
    return response.text, driver


def get_project_id(driver, auth):
    ''' Method to get project id of first process in process list. '''
    access_token, driver = get_access_token(driver, auth)
    token = {"Authorization": 'Bearer ' + access_token}
    response = requests.get(driver.api['url'] + '/api/1.0/' + driver.api['workspace'] + '/project', headers=token)
    driver.log.append('Acquired project id')
    return [json.loads(response.text)[0]['prj_uid'], token, driver]


def get_access_token(driver, auth):
    ''' Method to grab access token through password grant. '''
    payload = [
        ("grant_type", "password"),
        ("scope", "*"),
        ("client_id", auth['client_id']),
        ("client_secret", auth['client_secret']),
        ("username", auth['username']),
        ("password", auth['password'])
        ]
    response = requests.post(driver.api['url'] + '/' + driver.api['workspace'] + '/oauth2/token', data=payload)
    text = json.loads(response.text)
    driver.log.append('Acquired access token')
    return text['access_token'], driver


def get_response_code(driver, data):
    ''' Method to check the response code of a GET request to server URL provided. '''
    response = requests.get(data['server_url'])
    driver.log.append('Requested provided server URL')
    return response