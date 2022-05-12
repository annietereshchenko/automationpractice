class TestMainParameters:
    MAIN_PAGE_URL = 'http://automationpractice.com/index.php'
    SEARCH_DRESSES = 'dresses'
    SEARCH_NONEXISTENT_PRODUCT = 'NONEXISTENT_PRODUCT'
    NO_PRODUCT_FOUND_ALERT = f'No results were found for your search "{SEARCH_NONEXISTENT_PRODUCT}"'


class TestLoginParameters:
    LOGIN_PAGE_URL = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
    LOGIN_PAGE_HEADING = 'AUTHENTICATION'
    EMAIL = 'test18441@mail.com'
    FIRST_NAME = "Anna"
    LAST_NAME = 'Tereshchenko'
    PASSWORD = '123456789'
    UNREGISTERED_EMAIL = 't34s32t_1113320093@mail.com'
    AUTHENTICATION_FAILED_ERROR = 'There is 1 error\nAuthentication failed.'
    EMAIL_REQUIRED_ERROR = 'There is 1 error\nAn email address required.'
    PASSWORD_REQUIRED_ERROR = 'There is 1 error\nPassword is required.'


class TestCartParameters:
    CART_PAGE_URL = 'http://automationpractice.com/index.php?controller=order'
    EMPTY_CART_ALERT = 'Your shopping cart is empty.'
    ONE_PRODUCT_ADDED_TEXT = 'Cart 1 Product'
    ORDER_MESSAGE = "Your order on My Store is complete."
