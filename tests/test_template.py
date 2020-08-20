
# BaseTest, which extends unittest.TestCase. Instantiates webdriver.
from test_parent import BaseTest

# Method to run the test
from util import run_test

# Page classes
from page import *


''' All Test classes must extend BaseTest. '''
class TestName(BaseTest):

  ''' Maximum one test per class.
  Python's unittest convention requires that test methods begin with "test". '''
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
      data['class_instance'] = Class()

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
