#!/usr/bin/python3

import requests
import json

def parse_response():
    ''' Method to verify variable list can be parsed as JSON. '''
    try:
        json.loads(get_variable_list())
        return True
    except json.decoder.JSONDecodeError:
        return False

def get_variable_list():
    ''' Method to get variable list using project id. '''
    project_id, token = get_project_id()
    response = requests.get('https://mep.dev-ellucian-us.processmaker.com/api/1.0/mep/project/' + project_id + '/process-variables', headers=token)
    print(response.headers['content-type'])
    return response.text

def get_project_id():
    ''' Method to get project id of first process in process list. '''
    token = {"Authorization": 'Bearer ' + get_access_token()}
    response = requests.get('https://mep.dev-ellucian-us.processmaker.com/api/1.0/mep/project', headers=token)
    return (json.loads(response.text)[0]['prj_uid'], token)

def get_access_token():
    ''' Method to grab access token through password grant. '''
    payload = [("grant_type", "password"), ("scope", "*"), ("client_id", ''), ("client_secret", ''), ("username", ""), ("password", "")]
    response = requests.post('https://mep.dev-ellucian-us.processmaker.com/mep/oauth2/token', data=payload)
    print(response.headers['content-type'])
    text = json.loads(response.text)
    return text['access_token']

print(parse_response())