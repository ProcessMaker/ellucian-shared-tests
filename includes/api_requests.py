#!/usr/local/bin/python3

import json
import requests

def parse_response(auth):
    ''' Method to verify variable list can be parsed as JSON. '''
    try:
        json.loads(get_variable_list(auth))
        return True
    except json.decoder.JSONDecodeError:
        return False

def get_variable_list(auth):
    ''' Method to get variable list using project id. '''
    project_id, token = get_project_id(auth)
    response = requests.get('https://mep.dev-ellucian-us.processmaker.com/api/1.0/mep/project/' + project_id + '/process-variables', headers=token)
    return response.text

def get_project_id(auth):
    ''' Method to get project id of first process in process list. '''
    token = {"Authorization": 'Bearer ' + get_access_token(auth)}
    response = requests.get('https://mep.dev-ellucian-us.processmaker.com/api/1.0/mep/project', headers=token)
    return (json.loads(response.text)[0]['prj_uid'], token)

''' Once requests module is installed into Docker container, move this method to util.py. '''
def get_access_token(auth):
    ''' Method to grab access token through password grant. '''
    payload = [
        ("grant_type", "password"),
        ("scope", "*"),
        ("client_id", auth['client_id']),
        ("client_secret", auth['client_secret']),
        ("username", auth['username']),
        ("password", auth['password'])
        ]
    response = requests.post('https://mep.dev-ellucian-us.processmaker.com/mep/oauth2/token', data=payload)
    text = json.loads(response.text)
    return text['access_token']
