from pages.base_page import BasePage
from utilities.locators import *


class SignInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.sign_locator = SignInLocators

    def enter_email(self, email):
        self.element_to_be_clickable(self.sign_locator.EMAIL_ADDRESS_TEXT_FIELD).send_keys(email)

    def enter_password(self, password):
        self.element_to_be_clickable(self.sign_locator.PASSWORD_TEXT_FIELD).send_keys(password)

    def sign_in_using_valid_account(self):
        self.enter_email(self.valid_user_login)
        self.enter_password(self.valid_user_password)
        self.element_to_be_clickable(self.sign_locator.SIGN_IN_CONFIRM_BUTTON).click()

    def sign_in_using_invalid_account(self):
        self.enter_email(self.invalid_user_login)
        self.enter_password(self.invalid_user_password)
        self.element_to_be_clickable(self.sign_locator.SIGN_IN_CONFIRM_BUTTON).click()

    def sign_out(self):
        self.element_to_be_clickable(self.sign_locator.SIGN_OUT_BUTTON).click()

    def go_back_to_main_page(self):
        # move to base page
        self.element_to_be_clickable(self.sign_locator.SHOP_LOGO_BUTTON_TO_GO_TO_MAIN_PAGE).click()

    def check_is_sign_in_button_visible(self):
        return True if self.presence_of_element_located(self.sign_locator.SIGN_IN_BUTTON) else False

    def check_is_sign_out_button_visible(self):
        return True if self.presence_of_element_located(self.sign_locator.SIGN_OUT_BUTTON) else False

