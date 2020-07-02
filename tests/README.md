# Files 

( Links will be changed to master directory after merge )

## Tests

File | Class | Function | Success | Failure
--- | --- | --- | --- | ---
[`test_1_up.py`](https://github.com/ProcessMaker/ellucian-shared-tests/blob/kelly/tests/test_1_up.py "test_1_up.py") | TestLoginPage | Navigate to Login Page and verify login succeeds | `Main page loaded successfully` | `Main page failed to load`
[`test_2_1_mysql_version.py`](https://github.com/ProcessMaker/ellucian-shared-tests/blob/kelly/tests/test_2_1_mysql_version.py "test_2_1_mysql_version.py") | TestRDSVersions | Navigate to Case List Cache Builder page and verify correct MySQL version | `Correct MySQL version` | `Wrong MySQL version`
[`test_2_component_versions.py`](https://github.com/ProcessMaker/ellucian-shared-tests/blob/kelly/tests/test_2_component_versions.py "test_2_component_versions.py") | TestComponentVersions | Navigate to System Information page and verify correct component versions | `Correct [component]` | `Wrong [component]`
[`test_3_variables_load.py`](https://github.com/ProcessMaker/ellucian-shared-tests/blob/kelly/tests/test_3_variables_load.py "test_3_variables_load.py") | TestVariablesLoad | Navigate to applications page to get client id and client secret, then make api requests to verify process variables list loads correctly | `Variable list loaded` | `JSON Decode Error. First 20 chars of response: [first 20 chars of response]`
[`test_4_language_spot_check.py`](https://github.com/ProcessMaker/ellucian-shared-tests/blob/kelly/tests/test_4_language_spot_check.py "test_4_language_spot_check.py") | TestLanguageSpotCheck | Navigate to main page, change the url to different language versions, and verify there are no label placeholders instead of translated values | `Labels not found` | `Labels found`
[`test_5_plugin_versions.py`](https://github.com/ProcessMaker/ellucian-shared-tests/blob/kelly/tests/test_5_plugin_versions.py "test_5_plugin_versions.py") | TestPluginVersions | Navigate to Plugins Manager page and verify custom plugin versions are correct | <ul><li>`Correct [plugin] version, Enabled`</li><li>`All plugins found`</li></ul> | <ul><li>`Wrong [plugin] version, Enabled`</li><li>`Correct [plugin] version, Disabled`</li><li>`Wrong [plugin] version, Disabled`</li><li>`Not found: [plugins]`</li></ul>


#### Writing New Tests

File structure:

```
''' Import list.
'''
''' Python's unittest module. '''
import unittest

''' Selenium's WebDriverWait module. '''
from selenium.webdriver.support.ui import WebDriverWait

''' Selenium's By module. For use with WebDriverWait. '''
from selenium.webdriver.common.by import By

''' Selenium's expected_conditions module. For use with WebDriverWait. '''
from selenium.webdriver.support import expected_conditions as EC

''' BaseTest, which extends unittest.TestCase. Instantiates webdriver. '''
from test_parent import BaseTest

''' Methods to run the test and to log in to the provided server. '''
from util import run_test, login



''' All Test classes must extend BaseTest. '''
class TestName(BaseTest):
  
  ''' Maximum one test per class. '''
  def test_to_run(self):
  
    ''' List to hold log messages: the last string in the list is returned to PM4 output in run_test().
        Attached to the driver in login method and returned to the class attribute at the end of the test.
        Inherited from BaseTest.
    '''
    self.log
    
    ''' Webdriver instance to navigate through pages at server url.
        Object must be passed wherever it is used. Creating a new instance loses all navigation progress,
          including login.
        Inherited from BaseTest.
    '''
    self.driver
    
    ''' WebDriverWait instance to wait for elements to load on pages.
        Object may be reinstantiated.
        Inherited from BaseTest with default timeout 120 seconds.
    '''
    self.wait
    
    ''' Login method used at the beginning of each test navigation.
    login() returns driver.
    data is used here, but is defined in bootstrap.py file. Editors may underline data.
    '''
    self.driver = login(data, self.driver, self.log)
    
    ''' Reattach log to class attribute at end of test.
    '''
    self.log = self.driver.log
    

''' Main call. Only used in test file.
'''
if __name__ == "__main__":

    ''' Import __main__ to use as parameter for method calls.
    '''
    import __main__
    
    ''' Assign to data as a key, val pair in order to append relative paths and import files.
    repository_path and data are found in the bootstrap.py file for the Docker container.
    Must be referenced in __main__ call and then passed elsewhere. May be edited elsewhere. 
    '''
    data['repository_path'] = repository_path
    
    ''' You may add any key, value pairs to the data object. 
    Examples:
      data['word'] = 'apple'
      data['words'] = {'a': 'apple', 'b': 'banana', 'c': 'cantaloupe'}
      data['number'] = 100
      data['vegetables'] = ['pepper', 'spinach', 'squash']
    
    data comes with:
      data['server_url']
      data['server_workspace']
      data['username']
      data['password']
    '''
    
    ''' output is given back to bootstrap.py after the test is run.
    It is a dictionary with "result" and "message" key, value pairs.
    run_test() is the method that provides this dictionary. It requires the class name,
      the data object, and the __main__ module.
    '''
    output = run_test(TestLoginPage, data, __main__)
```

### Helpful Links 

(Hover for https:// address)
* [Python unittest Documentation](https://docs.python.org/3.5/library/unittest.html "https://docs.python.org/3.5/library/unittest.html")
* [Python unittest Source Code](https://github.com/python/cpython/tree/3.5/Lib/unittest "https://github.com/python/cpython/tree/3.5/Lib/unittest")
* [Selenium Documentation](https://selenium-python.readthedocs.io "https://selenium-python.readthedocs.io")
* [Selenium - Locating Elements](https://selenium-python.readthedocs.io/locating-elements.html "https://selenium-python.readthedocs.io/locating-elements.html")
* [Selenium - Waits](https://selenium-python.readthedocs.io/waits.html "https://selenium-python.readthedocs.io/waits.html")
* [Xpath cheatsheet](https://devhints.io/xpath "https://devhints.io/xpath")
