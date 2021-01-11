from selenium.webdriver.common.by import By


class MainPageLocators(object):
    CONTACT_BUTTON = (By.CSS_SELECTOR, '#contact-link')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '.login')
    WOMAN_SECTION_BUTTON = (By.CLASS_NAME, 'sfHoverForce')
    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//*[@id="authentication"]') # move to signin
    DRESSES_SECTION_BUTTON = ''
    TSHIRT_SECTION_BUTTON = ''
    SEARCH_FIELD = ''
    SEARCH_BUTTON = ''


class SignInLocators(object):
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '.login')  # copy z MainPageLocators
    EMAIL_ADDRESS_TEXT_FIELD = (By.XPATH, '//*[@id="email"]')
    PASSWORD_TEXT_FIELD = (By.XPATH, '//*[@id="passwd"]')
    SIGN_IN_CONFIRM_BUTTON = (By.XPATH, '//*[@id="SubmitLogin"]/span')
    SIGN_OUT_BUTTON = (By.CLASS_NAME, 'logout')
    MY_ACCOUNTS_LINKS = (By.CLASS_NAME, 'myaccount-link-list')  # Locator used to check did sign in process was success
    SHOP_LOGO_BUTTON_TO_GO_TO_MAIN_PAGE = (By.XPATH, '//*[@id="header_logo"]/a/img')


class SearchItemLocators(object):
    SEARCH_TEXT_BOX = (By.XPATH, '//*[@id="search_query_top"]')
    SEARCH_SUBMIT_BUTTON = (By.XPATH, '//*[@id="searchbox"]/button')
    PRODUCT_CONTAINER_FROM_PRODUCT_LIST = 'product-container'
    SEARCH_RESULT_COUNT = 'product-count'


class ProductPageLocators(object):
    FIRST_PRODUCT_ON_LIST = (By.CLASS_NAME, 'product-container')


class ProductDetailsPageLocators(object):
    PRODUCT_DETAILS_NAME = (By.XPATH, '//h1[@itemprop="name"]')
    ADD_PRODUCT_TO_CART = (By.XPATH, '//*[@id="add_to_cart"]/button/span')
    CONFIRMATION_POPUP_RESULT = (By.CLASS_NAME, 'icon-ok')


class CheckoutLocators(object):
    PROCEED_TO_CHECKOUT_BUTTON = (By.PARTIAL_LINK_TEXT, 'Proceed to checkout')
    PROCEED_TO_CHECKOUT_BUTTON_ON_ADDRESS = (By.XPATH, '//p/button[@type="submit"]')
    PROCEED_TO_CHECKOUT_BUTTON_ON_SHIPPING = (By.XPATH, '//p/button[@type="submit"]')
    AGREE_TO_SHIPPING_TERMS_CHECKBOX = (By.XPATH, '//*[@id="cgv"]')
    PAY_BY_BANK_WIRE_BUTTON = (By.CLASS_NAME, 'bankwire')
    PAY_BY_CHECK_BUTTON = (By.CLASS_NAME, 'cheque')
    CONFIRM_ORDER_BUTTON = (By.XPATH, '//*[@id="cart_navigation"]/button/span')
    SUCCESS_ALERT = (By.CLASS_NAME, 'alert-success')
    POPUP_ERROR_WHILE_NO_SHIPPING_TERMS = (By.CLASS_NAME, 'fancybox-error')
