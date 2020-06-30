#!/usr/local/bin

"""
Subclass unittest.TestCase
DONE --> add a class attribute that is a StringIO instance
--> --> to get page sources (DONE) and parse with regex (for HTML)
DONE --> add a class attribute that is a list
--> --> to add comments, notes, debug info, etc

Subclass unittest.TextTestRunner
DONE --> add _makeResult() method to call custom TextTestResult
--> define self.attribute (custom TestCase StringIO object) inside run() method
--> define result.attribute = self.attribute (from run() method) inside _makeResult() method
--> return result (_makeResult() method)

Subclass unittest.TextTestResult
--> 

Subclass unittest.TestSuite
--> Add 

Inside util run_test method
--> log object.read() to get logs


"""


import unittest

class CustomTestSuite(unittest.TestSuite):
    ''' Subclass TestSuite to add custom attributes. '''
    page_source = ''
    log = []

    def run(self, result): 
        ''' Add test case attributes to result. '''
        for test in self._tests:
            result.page_source = test.page_source
            result.log = test.log
        return super(CustomTestSuite, self).run(result)

class CustomTestLoader(unittest.TestLoader):
    ''' Subclass TestLoader to add custom TestSuite. '''
    suiteClass = CustomTestSuite

class CustomTextTestResult(unittest.TextTestResult):
    ''' Subclass TextTestResult to add custom results. '''

    def __init__(self, stream, descriptions, verbosity, log, page_source):
        """Initializes the test number generator, then calls super impl"""
        super(CustomTextTestResult, self).__init__(stream, descriptions, verbosity)
        self.log = log
        self.page_source = page_source


class CustomTextTestRunner(unittest.TextTestRunner):
    ''' Subclass TextTestRunner to add a custom test result. '''

    resultclass = CustomTextTestResult

    def run(self, test_suite):
        ''' Return the custom TextTestResult object. '''

        self.page_source = test_suite.page_source
        self.log = test_suite.log
        return super(CustomTextTestRunner, self).run(test_suite)

    def _makeResult(self):
        """Creates and returns a result instance that knows the count of test cases"""
        return CustomTextTestResult(self.stream, self.descriptions, self.verbosity, self.log, self.page_source)

