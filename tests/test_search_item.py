import unittest
from tests.base_test import BaseTest
from pages.main_page import *
from pages.search_item_page import *


class TestSearchItem(BaseTest):

    def test_search_item(self):
        search_item = SearchItemPage(self.driver)
        search_item.search_item_using_search_box('dress')
        search_item.get_products_from_product_list()

