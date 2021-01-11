from pages.base_page import BasePage
from utilities.locators import *


class ProductDetailsPage(BasePage):

    def __init__(self, driver):
        self.details_locator = ProductDetailsPageLocators
        super().__init__(driver)

    def get_product_name_from_product_details(self):
        element = self.visibility_of_element_located(self.details_locator.PRODUCT_DETAILS_NAME)
        return element.text

    def add_product_to_cart(self):
        self.element_to_be_clickable(self.details_locator.ADD_PRODUCT_TO_CART).click()

    def check_does_confirmation_popup_visible(self):
        return self.visibility_of_element_located(self.details_locator.CONFIRMATION_POPUP_RESULT)

