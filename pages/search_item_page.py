from pages.base_page import BasePage
from pages.products_page import ProductsPage
from utilities.locators import *


class SearchItemPage(BasePage):
    # move to header
    def __init__(self, driver):
        super().__init__(driver)
        self.search_locator = SearchItemLocators

    def search_item_using_search_box(self, searched_item):
        self.element_to_be_clickable(self.search_locator.SEARCH_TEXT_BOX).send_keys(searched_item)
        self.element_to_be_clickable(self.search_locator.SEARCH_SUBMIT_BUTTON).click()
        search_product_results = ProductsPage(self.driver)
        return search_product_results

    def get_products_from_product_list(self):
        return self.find_all_elements(self.search_locator.PRODUCT_CONTAINER_FROM_PRODUCT_LIST)
