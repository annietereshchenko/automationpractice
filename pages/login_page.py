from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def get_text_of_login_page_heading(self):
        return self.get_text_of_element(LoginPageLocators.SIGN_IN_PAGE_HEADING)

    def enter_email(self, email):
        self.send_keys(LoginPageLocators.EMAIL, email)

    def enter_password(self, password):
        self.send_keys(LoginPageLocators.PASSWORD, password)

    def click_on_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    def is_sign_out_button_displayed(self):
        return self.is_element_present(*MainPageLocators.SIGH_OUT_BUTTON)

    def get_account_name_text(self):
        return self.get_text_of_element(MainPageLocators.ACCOUNT_NAME)

    def get_text_of_failed_authentication(self):
        return self.get_text_of_element(LoginPageLocators.WARNING_MSG)
