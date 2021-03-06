# Overview

This repository consist of a series of Selenium tests that will be used to automatically validate changes between the shared ProcessMaker and Ellucian architectures.

## Trogdor

These tests will ultimately be executed within a PM4 custom instance dubbed "Trogdor". Trogdor processes will be initiated via CI/API and then will execute the tests in this repository against the environment specified in the API call. Once the tests have completed a report of the results will be provided, and in certain cases it will trigger a follow up action in the CI pipeline.

### Inheritance in Tests

In Trogdor, a custom selenium docker container is initialized with the contents of the repository. The script which executes the tests inside of this container, is setup to add the inludes/ dir of this repository into the PYTHONPATH, so that those classes may be reused across individual tests.

### Enabling a Test for Execution

In Trogdor, it will parse the config.json file of this repository in order to determine which tests to run. Once you are satisfied with the test, add it to the config file in order to execute it within Trogdor.

### Configuring a Test Run

When Trogdor is being executed, you must specify which environment to test and which test suite to execute. The following parameters are required:
* server_url: the URL for the ProcessMaker instance being tested (i.e. https://workspace.combined-dev.processmaker.com)
* server_workspace: The workspace to run the test against (i.e. workspacetest)
* repository: The location of a publicly accessible git repository containing tests to run (i.e. this page!)
* branch: the desired branch in the specified repository that you want to execute (i.e. stm-launch)
* username: the username used to login and run selenium UI tests
* password: the password used to login and run selenium UI tests


## Developing Tests Locally

#### Local System Requirements

You can develop and run tests locally. In order to do so, you must have the following:

* [Python 3.6.9](https://www.python.org) or above
* [Pip](https://pip.pypa.io/en/stable/installing/)
* [Selenium](https://www.selenium.dev)
* [Chrome](https://www.google.com/chrome/)
* [ChromeDriver 80.0.3987.106](https://chromedriver.chromium.org/getting-started) or above

* [Homebrew](https://brew.sh) (macOS only)

For testing API requests, you must have:

* [Python's requests module](https://requests.readthedocs.io/en/master/)

#### Installing Locally

* Install pip && `pip install selenium`
* `brew cask install chromedriver` (macOS only)
* Add chromedriver to PATH
* Clone the repository into a directory

#### Running Tests Locally

* Create `__init__.py` in root directory
* Write and save this line:
  * `data = {"server_url": "your/pm3/server/url/here", "server_workspace": "your/server/workspace/here", "username": "your/username/here", "password": "your/password/here"}`
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

#### [`/includes` Directory](https://github.com/ProcessMaker/ellucian-shared-tests/tree/master/includes "/includes Directory")
* Subclasses of `unittest` classes
* `BaseTest` from which test files inherit
* Helper methods
* `JSON` dictionary of plugin versions, component versions, and languages

#### [`/tests` Directory](https://github.com/ProcessMaker/ellucian-shared-tests/tree/master/tests "/tests Directory")
* Test cases
