from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from test_data.test_data import TestCartParameters as TD
from common_logic import CommonLogic


class TestCart:
    def test_open_cart_page(self, browser):
        main_page = MainPage(browser)
        cart_page = CartPage(browser)
        main_page.click_on_cart_button()
        assert cart_page.current_url() == TD.CART_PAGE_URL

    def test_empty_cart(self, browser):
        main_page = MainPage(browser)
        cart_page = CartPage(browser)
        main_page.click_on_cart_button()
        assert cart_page.get_text_of_empty_cart_alert() == TD.EMPTY_CART_ALERT

    def test_add_random_product_to_cart_check_counter(self, browser):
        main_page = MainPage(browser)
        product_page = ProductPage(browser)
        main_page.open_random_product()
        product_page.add_product_to_cart()
        product_page.close_addition_pop_up()
        assert main_page.get_text_of_cart() == TD.ONE_PRODUCT_ADDED_TEXT

    def test_add_random_product_to_cart_check_product_name_in_cart(self, browser):
        main_page = MainPage(browser)
        product_page = ProductPage(browser)
        cart_page = CartPage(browser)
        main_page.open_random_product()
        product_name = product_page.get_product_name()
        product_page.add_product_to_cart()
        product_page.close_addition_pop_up()
        main_page.click_on_cart_button()
        assert product_name == cart_page.get_name_of_added_product()

    def test_place_order_user_is_logged_in(self, browser):
        main_page = MainPage(browser)
        product_page = ProductPage(browser)
        cart_page = CartPage(browser)
        common_logic = CommonLogic(browser)
        common_logic.login_with_registered_user()
        main_page.click_on_logo()
        main_page.open_random_product()
        product_page.add_product_to_cart()
        product_page.close_addition_pop_up()
        main_page.click_on_cart_button()
        cart_page.click_on_proceed_to_checkout_button()
        cart_page.click_on_checkout_in_address_step_button()
        cart_page.click_on_terms_of_service_checkbox()
        cart_page.click_on_checkout_in_shipping_step_button()
        cart_page.select_bank_wire_payment_method()
        cart_page.click_on_confirm_order_button()
        assert cart_page.get_order_completed_msg() == TD.ORDER_MESSAGE

    def test_place_order_user_is_logged_in_check_empty_cart(self, browser):
        main_page = MainPage(browser)
        product_page = ProductPage(browser)
        cart_page = CartPage(browser)
        common_logic = CommonLogic(browser)
        common_logic.login_with_registered_user()
        main_page.click_on_logo()
        main_page.open_random_product()
        product_page.add_product_to_cart()
        product_page.close_addition_pop_up()
        main_page.click_on_cart_button()
        cart_page.click_on_proceed_to_checkout_button()
        cart_page.click_on_checkout_in_address_step_button()
        cart_page.click_on_terms_of_service_checkbox()
        cart_page.click_on_checkout_in_shipping_step_button()
        cart_page.select_bank_wire_payment_method()
        cart_page.click_on_confirm_order_button()
        main_page.click_on_cart_button()
        assert cart_page.get_text_of_empty_cart_alert() == TD.EMPTY_CART_ALERT

    def test_place_order_user_is_not_logged_in(self, browser):
        main_page = MainPage(browser)
        product_page = ProductPage(browser)
        cart_page = CartPage(browser)
        common_logic = CommonLogic(browser)
        main_page.open_random_product()
        product_page.add_product_to_cart()
        product_page.close_addition_pop_up()
        main_page.click_on_cart_button()
        cart_page.click_on_proceed_to_checkout_button()
        common_logic.login_with_registered_user_during_ordering()
        cart_page.click_on_checkout_in_address_step_button()
        cart_page.click_on_terms_of_service_checkbox()
        cart_page.click_on_checkout_in_shipping_step_button()
        cart_page.select_bank_wire_payment_method()
        cart_page.click_on_confirm_order_button()
        assert cart_page.get_order_completed_msg() == TD.ORDER_MESSAGE
