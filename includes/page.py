#!/usr/local/bin/python3

from element import *
from locators import *
import util
import api_requests
from selenium.webdriver.support.expected_conditions import visibility_of_element_located as visible
from selenium.webdriver.support.expected_conditions import frame_to_be_available_and_switch_to_it
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep


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
        self.page_url = self.data['server_url'].rstrip("/")
        self.wait = WebDriverWait(self.driver, 30)

    def server_check(self):
        ''' Check if the server gives a 400 or 500 response code. '''
        server_response = str(api_requests.get_response_code(self.data))
        self.driver.log.append(server_response)

        if '50' in server_response or '40' in server_response:
            return False
        return True

    def go_to_page(self, url=''):
        ''' Navigates to page_url:
                provided through config task on Trogdor server
                or through data defined in local __init__ file.
        '''
        if self.server_check():
            if url:
                self.driver.get(url)
            else:
                self.driver.get(self.page_url)
            return True
        return False


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
    Endpoint: login/login
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
    locator = (LoginPageLocators.USERNAME)[1]


class PasswordFieldElement(BasePageElement):
    """ Class to get password field using specified locator. """

    # Locator for search box where string is entered
    locator = (LoginPageLocators.PASSWORD)[1]

class WorkspaceFieldElement(BasePageElement):
    """ Class to get workspace field using specified locator. """

    # Locator for workspace field where string is entered
    locator = (LoginPageLocators.WORKSPACE)[1]


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


    def login(self):
        ''' Function to log user in to workspace.
        '''
        if not self.go_to_page():
            return False

        # Login
        self.username_field_element = self.data['username']
        self.password_field_element = self.data['password']
        self.workspace_field_element = self.data['server_workspace']
        submit_button_element = self.wait.until(visible(LoginPageLocators.SUBMIT_BUTTON))
        submit_button_element.click()
        self.driver.log.append('Credentials submitted')

        util.timezone_check(self.driver)

        return True

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
    Home Page
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


class HomePage(BasePage):
    """ Home Page actions.

        HomePageLocators are found in /includes/locators.py.
    """

    def __init__(self, driver, data):
        ''' Instantiate HomePage class. '''
        super(HomePage, self).__init__(driver, data)
        self.page_url = self.page_url + '/sys' + self.data['server_workspace'] +\
            '/en/ellucianux/cases/main'

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
        ''' Instantiate AdminPage class. '''
        super(AdminPage, self).__init__(driver, data)
        self.page_url = self.page_url + '/sys' + self.data['server_workspace'] +\
            '/en/ellucianux/setup/main'
        # self.wait.until(frame_to_be_available_and_switch_to_it(AdminPageLocators.ADMIN_IFRAME))

    def get_case_list_cache_builder(self):
        ''' Get text in Case List Cache Builder. '''
        self.driver.log.append('Navigate to Case List Cache Builder panel')
        self.go_to_page(self.data['server_url'] + '/sys' + self.data['server_workspace'] +\
            '/en/ellucianux/setup/appCacheViewConf')

        # Wait for page to load
        sleep(2)

        self.driver.log.append('Grabbing Case List Cache Builder text')
        workflow_applications_cache_info = self.wait.until(visible(AdminPageLocators.WORKFLOW_APPLICATIONS_CACHE_INFO))
        while not workflow_applications_cache_info.text:
            workflow_applications_cache_info = self.wait.until(visible(AdminPageLocators.WORKFLOW_APPLICATIONS_CACHE_INFO))
        return workflow_applications_cache_info.text

    def get_system_information(self):
        ''' Get text in System Information.'''
        self.driver.log.append('Navigate to System Information panel')
        self.go_to_page(self.data['server_url'] + '/sys' + self.data['server_workspace'] + '/en/ellucianux/setup/systemInfo?option=processInfo')

        # Wait for page elements to load
        sleep(2)

        self.driver.log.append('Getting Process Information table')
        process_information_table = self.wait.until(visible(AdminPageLocators.PROCESS_INFO_TABLE))

        while not process_information_table.text:
            process_information_table = self.wait.until(visible(AdminPageLocators.PROCESS_INFO_TABLE))

        system_information_table = self.wait.until(visible(AdminPageLocators.SYSTEM_INFO_TABLE))

        self.driver.log.append('Getting System Information table')
        while not system_information_table.text:
            system_information_table = self.wait.until(visible(AdminPageLocators.SYSTEM_INFO_TABLE))

        return (process_information_table.text, system_information_table.text)

    def get_custom_plugins(self):
        ''' Get list of plugins from /setup/pluginsMain. '''
        self.driver.log.append('Navigating to Custom Plugins page')
        self.go_to_page(self.data['server_url'] + '/sys' + self.data['server_workspace'] + '/en/ellucianux/setup/pluginsMain')


        # Add in while loop to wait for all plugins
        # Get number of plugins from expected_values.json

        # Wait for page elements to load
        sleep(2)

        self.driver.log.append('Find elements on Custom Plugins panel')
        self.wait.until(visible(AdminPageLocators.TABLE_ROW))
        self.elements = self.driver.find_elements(*AdminPageLocators.TABLE_ROW)

        # Add in check: last element in list .text is not empty

        return [element.text for element in self.elements]

    def get_enterprise_plugins(self):
        ''' Get list of plugins from /enterprise/addonsStore. '''
        self.driver.log.append('Navigating to Enterprise Plugins page')
        self.go_to_page(self.data['server_url'] + '/sys' + self.data['server_workspace'] + '/en/ellucianux/enterprise/addonsStore')


        # Add in while loop to wait for all plugins
        # Get number of plugins from expected_values.json

        # Wait for page elements to load
        sleep(2)

        self.driver.log.append('Finding elements on Enterprise Plugins panel')
        self.wait.until(visible(AdminPageLocators.TABLE_ROW))
        self.elements = self.driver.find_elements(*AdminPageLocators.TABLE_ROW)

        # Add in check: last element in list .text is not empty

        return [element.text for element in self.elements]

    def get_oauth_credentials(self):
        ''' Get oauth client id and client secret. '''
        self.driver.log.append('Navigating to Oauth Applications page')
        self.go_to_page(self.data['server_url'] + '/sys' + self.data['server_workspace'] + '/en/neoclassic/oauth2/applications')

        self.driver.log.append('Switching to iframe')
        self.driver.switch_to.frame(self.wait.until(visible(AdminPageLocators.ADMIN_IFRAME)))

        self.driver.log.append('Selecting first Oauth app table row')
        self.applications_table = self.wait.until(visible(AdminPageLocators.TABLE_ROW))
        self.applications_table.click()

        self.driver.log.append('Clicking on Oauth app detail button')
        self.app_detail_button = self.wait.until(visible(AdminPageLocators.OAUTH_APP_DETAIL_BUTTON))
        self.app_detail_button.click()

        self.driver.log.append('Viewing Oauth app detail')
        oauth_credentials = self.wait.until(visible(AdminPageLocators.OAUTH_APP_DETAIL_WINDOW))
        while not oauth_credentials.text:
            oauth_credentials = self.wait.until(visible(AdminPageLocators.OAUTH_APP_DETAIL_WINDOW))

        return oauth_credentials.text

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
        self.page_url = self.data['server_url'] + '/sys' + self.data['server_workspace'] +\
            '/en/ellucianux/processes/main'

    def is_loaded(self):
        ''' Verify Designer Page loads after login. '''
        self.wait = WebDriverWait(self.driver, 5)
        self.driver.log.append('Waiting for Designer page to load')
        try:
            self.driver.switch_to.frame(self.driver.find_element(*DesignerPageLocators.MAIN_IFRAME))
            self.driver.log.append('Designer page loaded in 5 seconds successfully')
            return True
        except:
            self.driver.log.append('Designer page failed to load in 5 seconds')
            return False

    def open_workflow(self):
        ''' Open Dynaform Styling workflow. '''
        self.driver.switch_to.frame(self.wait.until(visible(DesignerPageLocators.MAIN_IFRAME)))
        try:
            self.wait.until(visible(DesignerPageLocators.DYNAFORM_STYLING_ROW))
            element = self.driver.find_element(*DesignerPageLocators.DYNAFORM_STYLING_ROW)
            action = ActionChains(self.driver)
            action.double_click(on_element=element)
            action.perform()
            self.driver.log.append('Loading workflow')
        except:
            self.driver.log.append('Workflow failed to load')

    def open_workflow_dynaforms(self):
        ''' Open the Dynaforms option on the Process Object nav bar. '''
        try:
            self.driver.find_element(*DesignerPageLocators.DYNAFORMS_PROJECT_OBJECT).click()
            self.driver.log.append('Loading Dynaforms')
        except:
            self.driver.log.append('Dynaforms failed to load')

    def open_workflow_triggers(self):
        ''' Open the Triggers option on the Process Object nav bar. '''
        try:
            self.driver.find_element(*DesignerPageLocators.TRIGGERS_PROJECT_OBJECT).click()
            self.driver.log.append('Loading Triggers')
        except:
            self.driver.log.append('Triggers failed to load')

    def edit_row(self):
        ''' Edit the row containing Amount. '''
        try:
            #row = self.driver.find_element(*DesignerPageLocators.AMOUNT_ROW).find_element_by_xpath("..")
            self.driver.find_element(*DesignerPageLocators.AMOUNT_ROW_EDIT).click()
            self.driver.log.append('Loading Amount Edit page')
        except:
            self.driver.log.append('Amount Edit page failed to load')

    def click_plus_wizard(self):
        ''' Click the +Wizard button. '''
        try:
            self.driver.find_element(*DesignerPageLocators.PLUS_WIZARD_BUTTON).click()
            self.driver.log.append('Loading +Wizard triggers page')
        except:
            self.driver.log.append('+Wizard triggers page failed to load')

    def click_preview(self):
        ''' Click on preview button. '''
        try:
            self.wait.until(visible(DesignerPageLocators.PREVIEW_BUTTON)).click()
            self.driver.log.append('Loading Preview')
        except:
            self.driver.log.append('Preview failed to load')

    def new_project_has_two_options(self):
        ''' Method to verify that New dropdown menu contains two elements. '''

        self.driver.log.append('Navigating to Designer page')
        self.go_to_page(self.page_url)

        self.driver.log.append('Clicking New Project button')
        self.driver.switch_to.frame(self.wait.until(visible(DesignerPageLocators.MAIN_IFRAME)))
        new_button = self.wait.until(visible(DesignerPageLocators.NEW_PROJECT_BUTTON))
        new_button.click()

        # Wait for page to load
        sleep(2)

        self.driver.log.append('Checking dropdown list for two options')
        dropdown_elements = self.driver.find_elements(*DesignerPageLocators.NEW_DROPDOWN_LIST)

        if len(dropdown_elements) == 2:
            self.driver.log.append('Two new project options found')
            return True
        self.driver.log.append('Incorrect number of new project options')
        return False

    def interactable_elements_are_tab_accessible(self, num_elements):
        ''' Method to verify that all interactable elements on a page can be tabbed through. '''
        self.driver.switch_to.frame(self.wait.until(visible(DesignerPageLocators.PREVIEW_IFRAME)))
        self.driver.log.append('Switched to preview iframe')
        sleep(2)
        actions = ActionChains(self.driver)
        for _ in range(num_elements):
            actions = actions.send_keys(Keys.TAB)
        actions.perform()
        sleep(2)
        element = self.driver.switch_to.active_element
        return element.text
        #return element.is_selected()

    def count_triggers(self):
        ''' Method to count the triggers available. '''
        self.driver.log.append('Counting available triggers')
        triggers = self.driver.find_elements(*DesignerPageLocators.PREDEFINED_TRIGGERS)
        sum_triggers = len(triggers)
        for trigger in triggers:
            if not trigger.is_displayed():
                sum_triggers -= 1
        return sum_triggers


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
