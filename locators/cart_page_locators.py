from selenium.webdriver.common.by import By


class CartPageLocators:
    EMPTY_CART_ALERT = (By.CLASS_NAME, 'alert')
    PRODUCT_NAME = (By.CSS_SELECTOR, '#cart_summary .product-name')
    PROCEED_TO_CHECKOUT_BUTTON = (By.CSS_SELECTOR, '.cart_navigation > a[title="Proceed to checkout"]')
    PROCEED_TO_CHECKOUT_IN_ADDRESS_STEP_BUTTON = (By.NAME, 'processAddress')
    PROCEED_TO_CHECKOUT_IN_SHIPPING_STEP_BUTTON = (By.NAME, 'processCarrier')
    TERMS_OF_SERVICE_CHECKBOX = (By.ID, 'cgv')
    PAY_BY_BANK_WIRE = (By.CLASS_NAME, 'bankwire')
    CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR, '#cart_navigation .button')
    ORDER_COMPLETED_MSG = (By.CSS_SELECTOR, '.cheque-indent .dark')
