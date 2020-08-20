
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

    def setUp(self):
        ''' Run before each test method. '''

        # Keep track of test failures without pausing tests midway
        self.assertionFailures = []

        # Log in to the server and check for 40x & 50x response codes
        login_page = LoginPage(self.driver, data)
        # Fail test immediately if login fails
        self.assertTrue(login_page.login())

    def tearDown(self):
        ''' Run after each test method. '''

        # Check for test failures added during execution
        self.assertEqual([], self.assertionFailures)

    def test_to_run(self):

        ''' List to hold log messages: the last string in the list is returned to PM4 output in run_test().
        Attached to the driver in BaseTest.
        Inherited from BaseTest.
        '''
        self.driver.log

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


''' Main call. Used in every test file.
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
