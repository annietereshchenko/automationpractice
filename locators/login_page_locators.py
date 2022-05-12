from selenium.webdriver.common.by import By


class LoginPageLocators:
    SIGH_IN_BUTTON = (By.CLASS_NAME, 'header_user_info')
    SIGN_IN_PAGE_HEADING = (By.CLASS_NAME, 'page-heading')
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'passwd')
    LOGIN_BUTTON = (By.ID, 'SubmitLogin')
    WARNING_MSG = (By.CLASS_NAME, 'alert')
