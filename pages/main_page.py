from pages.base_page import BasePage
from utilities.locators import *


class MainPage(BasePage):

    def __init__(self, driver):
        self.main_locator = MainPageLocators
        super().__init__(driver)

    def click_sign_in_button(self):
        self.element_to_be_clickable(self.main_locator.SIGN_IN_BUTTON).click()

    def check_is_create_account_button_visible(self):
        return self.element_to_be_clickable(self.main_locator.CREATE_ACCOUNT_BUTTON)
