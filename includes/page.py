#!/usr/local/bin/python3

from element import *
from locators import *
import util


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
    Classes:
        BasePageShell:
            Initializes driver, data, and page_url attributes.
            Includes go_to_page method.
            These attributes and methods are available to all BasePage classes
                and classes that inherit from BasePage and BasePageShell classes.

        BasePage:
            Includes click_requests_link, click_tasks_link,
                click_designer_link, click_admin_link, and click_avatar methods.
            These methods are available to all Page classes that inherit from
                BasePage classes.
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class BasePageShell(object):
    """ Base page shell class from which two classes inherit:
            BasePage
            LoginPage
    """

    def __init__(self, driver, data):
        ''' Initializes each page with three attributes:
                driver:
                    instantited in /includes/test_parent.py.
                data:
                    provided through config task on Trogdor server
                    or through data defined in local __init__ file.
                page_url:
                    provided in data.
        '''
        self.driver = driver
        self.data = data
        self.page_url = self.data['server_url']

    def go_to_page(self):
        ''' Navigates to page_url:
                provided through config task on Trogdor server
                or through data defined in local __init__ file.
        '''
        self.driver.get(self.page_url)


class BasePage(BasePageShell):
    """ Base page class from which other page classes inherit.

        These methods are made available to all Page classes, aside from LoginPage,
            because these navigation links are all available on each page.

        BasePageLocators are found in /includes/locators.py.
    """

    def click_home_link(self):
        ''' Locates and clicks on Requests link in navigation bar. '''
        element = self.driver.find_element(*BasePageLocators.HOME_LINK)
        element.click()

    def click_designer_link(self):
        ''' Locates and clicks on Designer link in navigation bar. '''
        element = self.driver.find_element(*BasePageLocators.DESIGNER_LINK)
        element.click()

    def click_dashboards_link(self):
        ''' Locates and clicks on Dashboards link in navigation bar. '''
        element = self.driver.find_element(*BasePageLocators.DASHBOARDS_LINK)
        element.click()

    def click_kpis_link(self):
        ''' Locates and clicks on KPIs link in navigation bar. '''
        element = self.driver.find_element(*BasePageLocators.KPIS_LINK)
        element.click()

    def click_admin_link(self):
        ''' Locates and clicks on Admin link in navigation bar. '''
        element = self.driver.find_element(*BasePageLocators.ADMIN_LINK)
        element.click()


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
    Login Page
    Endpoint: /login
    Classes:
        LoginPage:
            Reinitializes page_url attribute. self.driver and self.data are
                inherited from BasePageShell.
            Instantiates UsernameFieldElement and PasswordFieldElement.
            Includes login method.
            These attributes and methods are available to test classes.

        UsernameFieldElement:
            Includes locator attribute. Inherits self.element_type from
                BasePageElement.
            This attribute is available to class instances.

        PasswordFieldElement:
            Includes locator attribute. Inherits self.element_type from
                BasePageElement.
            This attribute is available to class instances.

        WorkspaceFieldElement:
            Includes locator attribute. Inherits self.element_type from
                BasePageElement.
            This attribute is available to class instances.

"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class UsernameFieldElement(BasePageElement):
    """ Class to get username field using specified locator. """

    # Locator for search box where string is entered
    locator = (*LoginPageLocators.USERNAME)


class PasswordFieldElement(BasePageElement):
    """ Class to get password field using specified locator. """

    # Locator for search box where string is entered
    locator = (*LoginPageLocators.PASSWORD)

class WorkspaceFieldElement(BasePageElement):
    """ Class to get workspace field using specified locator. """

    # Locator for workspace field where string is entered
    locator = (*LoginPageLocators.WORKSPACE)[1]


class LoginPage(BasePageShell):
    """ Login Page actions.

        LoginPageLocators are found in /includes/locators.py.
    """

    username_field_element = UsernameFieldElement('ID')
    password_field_element = PasswordFieldElement('ID')
    workspace_field_element = WorkspaceFieldElement('ID')

    def __init__(self, driver, data):
        ''' Instantiate LoginPage class. '''
        super(LoginPage, self).__init__(driver, data)
        self.page_url = self.page_url + '/login'

    def login(self):
        ''' Function to log user in to workspace.
        '''
        # Login
        self.username_field_element = self.data['username']
        self.password_field_element = self.data['password']
        self.workspace_field_element = self.data['server_workspace']
        submit_button_element = self.driver.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        submit_button_element.click()

        return self.driver


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
    Requests Page
    Endpoint: /requests
    Classes:
        RequestsPage:
            Reinitializes page_url attribute. self.driver and self.data are
                inherited from BasePage.
            Includes click_my_requests_button, click_in_progress_button,
                click_completed_button, and click_all_requests_button methods.
            These attributes and methods are available to test classes.
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
    Admin Page
    Endpoint: /admin/users
    Classes:
        AdminPage:
            Reinitializes page_url attribute. self.driver and self.data are
                inherited from BasePage.
            Includes click_users_tab, click_deleted_users_tab,
                click_users_button, click_groups_button, click_auth_clients_button,
                click_customize_ui_button, click_queue_management_button, and
                click_script_executors_button methods.
            These attributes and methods are available to test classes.
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class AdminPage(BasePage):
    """ Admin Page actions.

        AdminPageLocators are found in /includes/locators.py.
    """

    def __init__(self, driver, data):
        ''' Instantiate DesignerPage class. '''
        super(AdminPage, self).__init__(driver, data)
        self.page_url = self.page_url + '/admin/users'


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
    Designer Page
    Endpoint: /processes
    Classes:
        DesignerPage:
            Reinitializes page_url attribute. self.driver and self.data are
                inherited from BasePage.
            Includes click_processes_tab, click_categories_tab,
                click_archived_processes_tab, click_processes_button,
                click_scripts_button, click_screens_button, and
                click_environment_variables_button methods.
            These attributes and methods are available to test classes.
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class DesignerPage(BasePage):
    """ Designer Page actions.

        DesignerPageLocators are found in /includes/locators.py.
    """

    def __init__(self, driver, data):
        ''' Instantiate DesignerPage class. '''
        super(DesignerPage, self).__init__(driver, data)
        self.page_url = self.data['server_url'] + '/processes'


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
    Classes:
        NewPage:
            Page class skeleton for creating new page classes.

            Reinitializes page_url attribute. self.driver and self.data are
                inherited from BasePage.
            Includes go_to_page method inherited from BasePage.

"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
class NewPage(BasePage):
    ''' New Page actions.

        NewPageLocators are found in /includes/locators.py.
    '''


    def __init__(self, driver, data):
        ''' Instantiate NewPage class. '''
        super(NewPage, self).__init__(driver, data)
        self.page_url = self.data['server_url'] + '/newpage/route'

    def click_page_element(self):
        ''' Clicks on New Page element. '''
        element = self.driver.find_element(*NewPageLocators.NEW_PAGE_ELEMENT)
        element.click()
"""
