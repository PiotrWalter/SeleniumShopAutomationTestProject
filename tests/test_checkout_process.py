from tests.base_test import BaseTest
from pages.checkout_page import *


class TestCheckoutProcess(BaseTest):

    def test_popup_when_no_shipping_confirmation(self):
        checkout_page = CheckoutPage(self.driver)
        checkout_page.log_in_find_item_and_add_item()
        checkout_page.proceed_through_checkout_to_shipping_confirmation()
        checkout_page.proceed_to_checkout_on_shipping_details()
        self.assertTrue(checkout_page.check_is_error_shipping_popup_visible())

    def test_full_checkout(self):
        checkout_page = CheckoutPage(self.driver)
        checkout_page.log_in_find_item_add_item_and_check_out()
