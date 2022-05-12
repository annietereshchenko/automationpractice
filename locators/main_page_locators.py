from selenium.webdriver.common.by import By


class MainPageLocators:
    SIGH_IN_BUTTON = (By.CLASS_NAME, 'header_user_info')
    CART_BUTTON = (By.CSS_SELECTOR, 'a[title="View my shopping cart"]')
    SIGH_OUT_BUTTON = (By.CLASS_NAME, 'logout')
    ACCOUNT_NAME = (By.CLASS_NAME, 'account')
    SEARCH_FIELD = (By.ID, 'search_query_top')
    SEARCH_BUTTON = (By.NAME, 'submit_search')
    FOUND_PRODUCT_NAMES = (By.XPATH, '//div[@class="right-block"]//a[@class="product-name"]')
    PRODUCTS_LIST = (By.XPATH, '//a[@class="product-name"]')
    NO_PRODUCT_FOUND_ALERT = (By.CLASS_NAME, 'alert')
    WOMAN_CATEGORY = (By.CSS_SELECTOR, 'a[title="Women"]')
    TOP_CATEGORY = (By.CSS_SELECTOR, 'a[title="Tops"]')
    LOGO = (By.CLASS_NAME, 'logo')
