from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from pages.search_item_page import SearchItemPage
from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
from utilities.locators import *


class CheckoutPage(MainPage, SignInPage, SearchItemPage, ProductsPage, ProductDetailsPage):

    def __init__(self, driver):
        self.checkout_locators = CheckoutLocators
        super().__init__(driver)

    def proceed_to_checkout_button_click(self, locator):
        self.element_to_be_clickable(locator).click()

    def proceed_to_checkout_on_shipping_details(self):
        self.proceed_to_checkout_button_click(self.checkout_locators.PROCEED_TO_CHECKOUT_BUTTON_ON_SHIPPING)

    def agree_to_shipping_terms_click(self):
        self.presence_of_element_located(self.checkout_locators.AGREE_TO_SHIPPING_TERMS_CHECKBOX).click()

    def check_is_error_shipping_popup_visible(self):
        return self.presence_of_element_located(self.checkout_locators.POPUP_ERROR_WHILE_NO_SHIPPING_TERMS)

    def check_is_your_order_complete_confirmation_visible(self):
        return self.presence_of_element_located(self.checkout_locators.SUCCESS_ALERT)

    def proceed_through_checkout_to_shipping_confirmation(self):
        self.proceed_to_checkout_button_click(self.checkout_locators.PROCEED_TO_CHECKOUT_BUTTON)
        self.proceed_to_checkout_button_click(self.checkout_locators.PROCEED_TO_CHECKOUT_BUTTON)
        self.proceed_to_checkout_button_click(self.checkout_locators.PROCEED_TO_CHECKOUT_BUTTON_ON_ADDRESS)

    def proceed_through_whole_checkout_to_payment(self):
        self.proceed_through_checkout_to_shipping_confirmation()
        self.agree_to_shipping_terms_click()
        self.proceed_to_checkout_button_click(self.checkout_locators.PROCEED_TO_CHECKOUT_BUTTON_ON_SHIPPING)

    def pay_by_bank_wire(self):
        self.element_to_be_clickable(self.checkout_locators.PAY_BY_BANK_WIRE_BUTTON).click()
        self.element_to_be_clickable(self.checkout_locators.CONFIRM_ORDER_BUTTON).click()

    def pay_by_check(self):
        self.element_to_be_clickable(self.checkout_locators.PAY_BY_CHECK_BUTTON).click()
        self.element_to_be_clickable(self.checkout_locators.CONFIRM_ORDER_BUTTON).click()

    def log_in_find_item_and_add_item(self):
        # add this to helper
        self.click_sign_in_button()
        self.sign_in_using_valid_account()
        self.search_item_using_search_box('Faded Short Sleeve T-shirts')
        self.go_to_product_details()
        self.add_product_to_cart()

    def log_in_find_item_add_item_and_check_out(self):
        self.click_sign_in_button()
        self.sign_in_using_valid_account()
        self.search_item_using_search_box('Faded Short Sleeve T-shirts')
        self.go_to_product_details()
        self.add_product_to_cart()
        self.proceed_through_whole_checkout_to_payment()
        self.pay_by_check()

