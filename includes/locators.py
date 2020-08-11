#!/usr/local/bin/python3

from selenium.webdriver.common.by import By

class BasePageLocators(object):
    """ Class for Base Page locators. Navigation bar locators here. """
    HOME_LINK = (By.LINK_TEXT, 'Home')
    DESIGNER_LINK = (By.LINK_TEXT, 'Designer')
    DASHBOARDS_LINK = (By.LINK_TEXT, 'Dashboards')
    KPIS_LINK = (By.LINK_TEXT, 'KPIs')
    ADMIN_LINK = (By.LINK_TEXT, 'Admin')

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
    NEW_BUTTON = (By.ID, 'ext-gen35')
    NEW_DROPDOWN_LIST = (By.CLASS_NAME, 'x-menu-list-item')

class DashboardsPageLocators(object):
    """ Class for Dashboards Page locators. All Dashboards page locators here. """

class KPIsPageLocators(object):
    """ Class for KPIs Page locators. All KPIs page locators here. """

class AdminPageLocators(object):
    """ Class for Admin Page locators. All Admin page locators here. """
    ADMIN_IFRAME = (By.ID, 'adminFrame')
    ADMIN_SUB_FRAME = (By.ID, 'setup-frame')
