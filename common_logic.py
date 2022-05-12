from pages.login_page import LoginPage
from pages.main_page import MainPage
from test_data.test_data import TestLoginParameters as TD


class CommonLogic(LoginPage, MainPage):
    def login_with_registered_user(self):
        self.click_on_sign_in_button()
        self.enter_email(TD.EMAIL)
        self.enter_password(TD.PASSWORD)
        self.click_on_login()

    def login_with_registered_user_during_ordering(self):
        self.enter_email(TD.EMAIL)
        self.enter_password(TD.PASSWORD)
        self.click_on_login()

