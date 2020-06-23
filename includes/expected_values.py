#!/usr/local/bin/python3
""" Define class containing expected values to test against.
"""

class ExpectedValues:
    ''' Class to hold tables and lists for release tests. '''
    def __init__(self):
        # List of supported languages
        self.languages = ['en', 'es']

        # Dictionary of Infrastructure Components and their expected versions
        self.infrastructure_components = {
            "RDS": {
                "mysql": "5.7"
            },
            "System Information": {
                "php": "7.3.17",
                "nginx": "1.16.1",
                "pm3": "3.4.11"
            },
            "Custom Plugins": {
                "SSO_SAML": "3.2.7",
                "Ellucian Ethos Events": "1.3.0+012",
                "ppsEllucianLdap": "1.5.0",
                "Ellucian Ethos Integration": "1.5.0+950"
            },
            "Enterprise Plugins": {
                "data Reporting Tools": "1.1.15",
                "Enterprise Data Search": "3.2.3",
                "Multitenant Workspace Management": "3.1.6",
                "N InOutlook": "3.2.0",
                "ProcessDocumenter": "1.1.2",
                "advanced Dashboards": "3.0.2",
                "External Registration": "3.3.6",
                "pmBusinessRules": "3.1.3",
                "pmConnectors": "1.3.1",
                "Enhanced Login": "2.6.3",
                "pmFtpMonitor": "3.1.1",
                "pmGSuiteAuth": "1.1.1",
                "Input Document Uploader": "3.1.4",
                "Power Up": "3.1.4",
                "Reports": "3.5.2",
                "Service Level Agreement": "3.0.2",
                "SAML Authentication": "1.0.3",
                "Enhanced Home Experience": "1.2.0"
            }
        }