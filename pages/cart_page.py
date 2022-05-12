from pages.base_page import BasePage
from locators.cart_page_locators import CartPageLocators


class CartPage(BasePage):
    def get_text_of_empty_cart_alert(self):
        return self.get_text_of_element(CartPageLocators.EMPTY_CART_ALERT)

    def get_name_of_added_product(self):
        return self.get_text_of_element(CartPageLocators.PRODUCT_NAME)

    def click_on_proceed_to_checkout_button(self):
        self.find_element(CartPageLocators.PROCEED_TO_CHECKOUT_BUTTON).click()

    def click_on_checkout_in_address_step_button(self):
        self.find_element(CartPageLocators.PROCEED_TO_CHECKOUT_IN_ADDRESS_STEP_BUTTON).click()

    def click_on_terms_of_service_checkbox(self):
        self.find_element(CartPageLocators.TERMS_OF_SERVICE_CHECKBOX).click()

    def click_on_checkout_in_shipping_step_button(self):
        self.find_element(CartPageLocators.PROCEED_TO_CHECKOUT_IN_SHIPPING_STEP_BUTTON).click()

    def select_bank_wire_payment_method(self):
        self.find_element(CartPageLocators.PAY_BY_BANK_WIRE).click()

    def click_on_confirm_order_button(self):
        self.find_element(CartPageLocators.CONFIRM_ORDER_BUTTON).click()

    def get_order_completed_msg(self):
        return self.get_text_of_element(CartPageLocators.ORDER_COMPLETED_MSG)
