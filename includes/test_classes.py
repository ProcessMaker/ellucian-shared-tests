#!/usr/local/bin
"""
Classes to extend unittest classes.
"""

import unittest

class CustomTestSuite(unittest.TestSuite):
    ''' Subclass TestSuite to add custom attributes. '''
    log = []

    def run(self, result):
        ''' Add test case attributes to result. '''
        for test in self._tests:
            result.log = test.log
        return super(CustomTestSuite, self).run(result)

class CustomTestLoader(unittest.TestLoader):
    ''' Subclass TestLoader to add custom TestSuite. '''
    suiteClass = CustomTestSuite

class CustomTextTestResult(unittest.TextTestResult):
    ''' Subclass TextTestResult to add custom results. '''

    def __init__(self, stream, descriptions, verbosity, log):
        """Initializes the test number generator, then calls super impl"""
        super(CustomTextTestResult, self).__init__(stream, descriptions, verbosity)
        self.log = log


class CustomTextTestRunner(unittest.TextTestRunner):
    ''' Subclass TextTestRunner to add a custom test result. '''

    resultclass = CustomTextTestResult

    def run(self, test_suite):
        ''' Return the custom TextTestResult object. '''

        self.log = test_suite.log
        return super(CustomTextTestRunner, self).run(test_suite)

    def _makeResult(self):
        """Creates and returns a result instance that has custom attributes"""
        return CustomTextTestResult(self.stream, self.descriptions, self.verbosity, self.log)
