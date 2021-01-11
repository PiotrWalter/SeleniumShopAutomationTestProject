from pages.base_page import BasePage
from pages.product_details_page import ProductDetailsPage
from utilities.locators import *


class ProductsPage(BasePage):

    def __init__(self, driver):
        self.product_locator = ProductPageLocators
        self.details_locator = ProductDetailsPageLocators
        super().__init__(driver)

    def go_to_product_details(self):
        self.element_to_be_clickable(self.product_locator.FIRST_PRODUCT_ON_LIST).click()
        product_details_page = ProductDetailsPage(self.driver)
        return product_details_page
