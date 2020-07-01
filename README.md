# Ellucian Shared Tests Documentation

# Overview

Ellucian Shared Tests consist of a series of Selenium tests that will be used to automatically validate changes between the shared ProcessMaker and Ellucian architectures.

## Trogdor

These tests will ultimately be executed within a PM4 custom instance dubbed "Trogdor". Trogdor processes will be initiated via CI/API and then will execute the tests in this repository against the environment specified in the API call. Once the tests have completed a report of the results will be provided.

### Inheritance in Tests

In Trogdor, a custom selenium docker container is initialized with the contents of the repository. The script which executes the tests inside of this container, is setup to add the inludes/ dir of this repository into the PYTHONPATH, so that those classes may be reused across individual tests.

### Enabling a Test in Production

In Trogdor, it will parse the config.json file of this repository in order to determine which tests to run. Once you are satisfied with the test, add it to the config file in order to execute it within Trogdor.

## Developing Tests Locally

#### Local System Requirements

You can develop and run tests locally. In order to do so, you must have the following:

* [Python 3.6.9](https://www.python.org) or above
* [Pip](https://pip.pypa.io/en/stable/installing/)
* [Selenium](https://www.selenium.dev)
* [Chrome](https://www.google.com/chrome/)
* [ChromeDriver 80.0.3987.106](https://chromedriver.chromium.org/getting-started) or above

* [Homebrew](https://brew.sh) (macOS only)

#### Installing Locally

* Install pip && `pip install selenium`
* `brew cask install chromedriver` (macOS only)
* Add chromedriver to PATH
* Clone the repository into a directory

#### Running Tests Locally

* Create `__init__.py` in root directory
* Write and save this line:
  * `data = {"server_url": "your/pm4/server/url/here", "server_workspace": "your/server/workspace/here", "username": "your/username/here", "password": "your/password/here"}`
* Navigate to `/tests` folder
* Execute test with `./test_you_want_to_run.py`
  * Note: If test is not executable, run `chmod +x test_you_want_to_run.py`

Notes: 
  * If you want to view the tests running in the browser, comment out this line in `/includes/test_parent.py`:
    * `# chrome_options.add_argument("--headless")`
  * If you want to view python unittest results in your terminal, add this line to the bottom of the test file:
    * `print(output)`
  * Sometimes tests will fail to run if there is an `__init__.py` in the `/tests` directory. Remove this file if it exists.
  
#### Writing Tests Locally

( Below suggestions may be redundant with use of conditional imports and ENV variable in Docker container, TBD )
Inside each test file:
  * Add these lines to the top of your imports:
    * `from sys import path`
    * `path.append('../')`
  * Change these lines:
    * `from test_parent` to `from includes.test_parent`
    * `from util` to `from includes.util`
    * `from api_requests` to `from includes.api_requests`
  * Add this line:
    * `from __init__ import data`

## Files 

( Links will be changed to master directory after merge )

#### [`/includes` Directory](https://github.com/ProcessMaker/ellucian-shared-tests/tree/kelly/includes "/includes Directory")

[`/includes/api_requests.py`](https://github.com/ProcessMaker/ellucian-shared-tests/blob/kelly/includes/api_requests.py "api_requests.py")
Method | Function | Parameters | Uses
--- | --- | --- | ---
`get_access_token` | <ul><li>Uses post request to acquire access token through password grant</li><li>returns access token and driver</li></ul> | `driver, auth` | <ul><li>`driver` passes url, workspace, and log</li><li>`auth` passes password grant body key, value pairs</li></ul>
`get_project_id` | <ul><li>Uses access token to get request project ID of first process on processes page</li><li>returns project id, header token, and driver</li></ul> | `driver, auth` | <ul><li>`driver` passes url, workspace, and log</li><li>`auth` passes password grant body key, value pairs</li></ul>
`get_variable_list`| <ul><li>Uses project id to get request variable list of process</li><li>returns response text and driver</li></ul> | `driver, auth` | <ul><li>`driver` passes url, workspace, and log</li><li>`auth` passes password grant body key, value pairs</li></ul>
`parse_response` | <ul><li>Parses variable list with `json.loads()` to verify GUI list will be populated</li><li>returns boolean and driver</li></ul> | `driver, auth` | <ul><li>`driver` passes url, workspace, and log</li><li>`auth` passes password grant body key, value pairs</li></ul>

[`/includes/util.py`](https://github.com/ProcessMaker/ellucian-shared-tests/blob/kelly/includes/util.py "util.py")
Method | Function | Parameters | Uses
--- | --- | --- | ---
`run_test` | <ul><li>Loads and runs test suite, redirects unittest results to memory stream</li><li>returns PM4-friendly output</li></ul> | `classname, data, modulename` | <ul><li>`classname` passes the test class name</li><li>`data` passes the configuration in PM4's config task</li><li>`modulename` passes `__main__` from test file</li></ul>
`parse_log_error`| <ul><li>Searches text for `'ERROR'`</li><li>returns `ERROR` message</li></ul> | `log_message` | <ul><li>`log_message` passes `HTML` page source</li></ul>
`parse_log_warning`| <ul><li>Searches text for `'WARNING'`</li><li>returns `WARNING` message</li></ul> | `log_message` | <ul><li>`log_message` passes `HTML` page source</li></ul>
