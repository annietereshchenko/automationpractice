from pages.login_page import LoginPage
from pages.main_page import MainPage
from test_data.test_data import TestLoginParameters as TD


class TestLogin:
    def test_open_login_page(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        main_page.click_on_sign_in_button()
        assert login_page.current_url() == TD.LOGIN_PAGE_URL

    def test_open_login_check_heading(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        main_page.click_on_sign_in_button()
        assert login_page.get_text_of_login_page_heading() == TD.LOGIN_PAGE_HEADING

    def test_login_with_registered_user(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        main_page.click_on_sign_in_button()
        login_page.enter_email(TD.EMAIL)
        login_page.enter_password(TD.PASSWORD)
        login_page.click_on_login()
        assert login_page.is_sign_out_button_displayed() == 1

    def test_login_with_registered_user_check_user_name(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        main_page.click_on_sign_in_button()
        login_page.enter_email(TD.EMAIL)
        login_page.enter_password(TD.PASSWORD)
        login_page.click_on_login()
        assert login_page.get_account_name_text() == f'{TD.FIRST_NAME} {TD.LAST_NAME}'

    def test_login_with_unregistered_user(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        main_page.click_on_sign_in_button()
        login_page.enter_email(TD.UNREGISTERED_EMAIL)
        login_page.enter_password(TD.PASSWORD)
        login_page.click_on_login()
        assert login_page.get_text_of_failed_authentication() == TD.AUTHENTICATION_FAILED_ERROR

    def test_login_leave_email_field_empty(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        main_page.click_on_sign_in_button()
        login_page.enter_password(TD.PASSWORD)
        login_page.click_on_login()
        assert login_page.get_text_of_failed_authentication() == TD.EMAIL_REQUIRED_ERROR

    def test_login_leave_passwd_field_empty(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        main_page.click_on_sign_in_button()
        login_page.enter_email(TD.EMAIL)
        login_page.click_on_login()
        assert login_page.get_text_of_failed_authentication() == TD.PASSWORD_REQUIRED_ERROR
