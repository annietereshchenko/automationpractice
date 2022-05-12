from random import randint
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def click_on_sign_in_button(self):
        self.find_element(MainPageLocators.SIGH_IN_BUTTON).click()

    def click_on_cart_button(self):
        self.find_element(MainPageLocators.CART_BUTTON).click()

    def enter_product_name(self, product_name):
        self.send_keys(MainPageLocators.SEARCH_FIELD, product_name)

    def click_on_search_button(self):
        self.find_element(MainPageLocators.SEARCH_BUTTON).click()

    def get_count_of_dresses(self):
        return self.get_count_of_elements(MainPageLocators.FOUND_PRODUCT_NAMES)

    def does_found_product_contain_dress_in_name(self, search):
        product_names = self.get_text_of_elements(MainPageLocators.FOUND_PRODUCT_NAMES)
        for product in product_names:
            if search not in product:
                return False
        return True

    def open_random_product(self):
        product_list = self.find_elements(MainPageLocators.PRODUCTS_LIST)
        random_index = randint(0, 6)
        product_list[random_index].click()
        return random_index + 1

    def get_text_of_no_product_found_alert(self):
        return self.get_text_of_element(MainPageLocators.NO_PRODUCT_FOUND_ALERT)

    def move_mouse_to_women_category(self):
        self.move_cursor_to_element(MainPageLocators.WOMAN_CATEGORY)

    def is_top_category_visible(self):
        return self.is_element_displayed(MainPageLocators.TOP_CATEGORY)

    def get_text_of_cart(self):
        return self.get_text_of_element(MainPageLocators.CART_BUTTON)

    def click_on_logo(self):
        self.find_element(MainPageLocators.LOGO).click()
