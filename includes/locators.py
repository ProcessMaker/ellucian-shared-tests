#!/usr/local/bin/python3

from selenium.webdriver.common.by import By

class BasePageLocators(object):
    """ Class for Base Page locators. Navigation bar locators here. """
    HOME_LINK = (By.ID, 'CASES')
    DESIGNER_LINK = (By.ID, 'PROCESSES')
    DASHBOARDS_LINK = (By.ID, 'DASHBOARD')
    KPIS_LINK = (By.ID, 'DASHBOARD+')
    ADMIN_LINK = (By.ID, 'SETUP')

class LoginPageLocators(object):
    """ Class for Login Page locators. All Login page locators here. """
    USERNAME = (By.ID, 'form[USR_USERNAME]')
    PASSWORD = (By.ID, 'form[USR_PASSWORD_MASK]')
    WORKSPACE = (By.ID, 'form[USER_ENV]')
    SUBMIT_BUTTON = (By.ID, 'form[BSUBMIT]')

class HomePageLocators(object):
    """ Class for Designer Page locators. All Designer page locators here. """
    CASES_IFRAME = (By.ID, 'casesFrame')
    CASES_SUB_FRAME = (By.ID, 'casesSubFrame')

class DesignerPageLocators(object):
    """ Class for Designer Page locators. All Designer page locators here. """
    MAIN_IFRAME = (By.ID, 'frameMain')
    NEW_PROJECT_BUTTON = (By.ID, 'ext-gen35')
    NEW_DROPDOWN_LIST = (By.CLASS_NAME, 'x-menu-list-item')

    """ Locators requiring input """
    DYNAFORM_STYLING_ROW = (By.XPATH, "//div[contains(text(), 'Dynaform Styling')]")
    DYNAFORMS_PROJECT_OBJECT = (By.XPATH, "//a[contains(text(),'Dynaforms')]")
    TRIGGERS_PROJECT_OBJECT = (By.XPATH, "//a[contains(text(),'Triggers')]")

    AMOUNT_ROW = (By.XPATH, "//tr[contains(text(), 'Amount')]")
    AMOUNT_ROW_EDIT = (By.XPATH, "//span[contains(text(), 'Edit')]")
    PLUS_WIZARD_BUTTON = (By.XPATH, "//span[contains(text(), 'Wizard')]")
    
    PREVIEW_BUTTON = (By.XPATH, "//div[@class='ui-layout-north fd-toolbar-designer ui-layout-pane ui-layout-pane-north']//div[4]//img[1]")
    PREVIEW_IFRAME = (By.ID, 'pm-dynaform-preview-iframe')
    PREDEFINED_TRIGGERS = (By.CLASS_NAME, 'pmui-accordion-item-container')

class DashboardsPageLocators(object):
    """ Class for Dashboards Page locators. All Dashboards page locators here. """

class KPIsPageLocators(object):
    """ Class for KPIs Page locators. All KPIs page locators here. """

class AdminPageLocators(object):
    """ Class for Admin Page locators. All Admin page locators here. """
    ADMIN_IFRAME = (By.ID, 'adminFrame')
    ADMIN_SUB_IFRAME = (By.ID, 'setup-frame')

    """ Locators for iframes loaded through direct links """
    WORKFLOW_APPLICATIONS_CACHE_INFO = (By.ID, 'ext-gen20')
    PROCESS_INFO_TABLE = (By.ID, 'ext-gen13-gp-section-Process Information-bd')
    SYSTEM_INFO_TABLE = (By.ID, 'ext-gen13-gp-section-System information-bd')
    TABLE_ROW = (By.CLASS_NAME, 'x-grid3-row')
    OAUTH_APP_DETAIL_BUTTON = (By.ID, 'ext-gen42')
    OAUTH_APP_DETAIL_WINDOW = (By.ID, 'ext-comp-1010')
