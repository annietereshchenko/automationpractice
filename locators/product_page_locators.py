from selenium.webdriver.common.by import By


class ProductPageLocators:
    ADD_PRODUCT_TO_CART_BUTTON = (By.NAME, 'Submit')
    PRODUCT_ADDED_TO_CART_MSG = (By.CLASS_NAME, 'icon-ok')
    CROSS_ICON = (By.CLASS_NAME, 'cross')
    ADD_PRODUCT_TO_CART_BUTTON_DISABLED = (By.CSS_SELECTOR, '.disabled')
    PRODUCT_NAME = (By.XPATH, '//h1[@itemprop="name"]')
