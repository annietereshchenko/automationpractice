from pages.base_page import BasePage
from locators.product_page_locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        self.find_element(ProductPageLocators.ADD_PRODUCT_TO_CART_BUTTON).click()
        self.wait_fo_invisibility_of_element(ProductPageLocators.ADD_PRODUCT_TO_CART_BUTTON_DISABLED)

    def is_the_product_addition_message_displayed(self):
        return self.is_element_displayed(ProductPageLocators.PRODUCT_ADDED_TO_CART_MSG)

    def close_addition_pop_up(self):
        self.find_element(ProductPageLocators.CROSS_ICON).click()

    def get_product_name(self):
        return self.get_text_of_element(ProductPageLocators.PRODUCT_NAME)
