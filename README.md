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

#### Installing & Running Locally

* Install pip && `pip install selenium`
* `brew cask install chromedriver` (macOS only)
* Add chromedriver to PATH
* Clone the repository into a directory
* Navigate to tests folder
* Execute test file using `python3 test_file.py`
