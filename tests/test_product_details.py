from tests.base_test import BaseTest
from pages.search_item_page import *
from pages.products_page import *
from pages.product_details_page import *


class TestProductDetails(BaseTest):

    def test_search_and_check_product_details(self):
        search_item = SearchItemPage(self.driver)
        product_page = ProductsPage(self.driver)
        product_details_page = ProductDetailsPage(self.driver)
        search_item.search_item_using_search_box('Faded Short Sleeve T-shirts')
        product_page.go_to_product_details()
        self.assertIn('Faded Short Sleeve T-shirts', product_details_page.get_product_name_from_product_details())

    def test_adding_product_to_cart(self):
        search_item = SearchItemPage(self.driver)
        product_page = search_item.search_item_using_search_box('Faded Short Sleeve T-shirts')
        product_details_page = product_page.go_to_product_details()
        product_details_page.add_product_to_cart()
        self.assertTrue(product_details_page.check_does_confirmation_popup_visible())

