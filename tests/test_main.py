from pages.main_page import MainPage
from pages.product_page import ProductPage
from test_data.test_data import TestMainParameters as TD


class TestLogin:
    def test_open_main_page(self, browser):
        main_page = MainPage(browser)
        assert main_page.current_url() == TD.MAIN_PAGE_URL

    def test_search_dresses_check_count(self, browser):
        main_page = MainPage(browser)
        main_page.enter_product_name(TD.SEARCH_DRESSES)
        main_page.click_on_search_button()
        assert main_page.get_count_of_dresses() == 5

    def test_search_dresses_check_found_products_names(self, browser):
        main_page = MainPage(browser)
        main_page.enter_product_name(TD.SEARCH_DRESSES)
        main_page.click_on_search_button()
        assert main_page.does_found_product_contain_dress_in_name(TD.SEARCH_DRESSES) is True

    def test_search_nonexistent_product(self, browser):
        main_page = MainPage(browser)
        main_page.enter_product_name(TD.SEARCH_NONEXISTENT_PRODUCT)
        main_page.click_on_search_button()
        assert main_page.get_text_of_no_product_found_alert() == TD.NO_PRODUCT_FOUND_ALERT

    def test_open_random_product(self, browser):
        main_page = MainPage(browser)
        product_page = ProductPage(browser)
        index = main_page.open_random_product()
        assert product_page.current_url() == \
               f'http://automationpractice.com/index.php?id_product={index}&controller=product'

    def test_hover_mouse_over_women_category(self, browser):
        main_page = MainPage(browser)
        main_page.move_mouse_to_women_category()
        assert main_page.is_top_category_visible() is True
