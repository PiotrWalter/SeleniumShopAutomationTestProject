import unittest
from tests.base_test import BaseTest
from pages.main_page import *
from pages.sign_in_page import *


class TestSignInPage(BaseTest):

    def test_sign_in_using_valid_account(self):
        main_page = MainPage(self.driver)
        sign_in = SignInPage(self.driver)
        main_page.click_sign_in_button()
        sign_in.sign_in_using_valid_account()
        self.assertTrue(sign_in.check_is_sign_out_button_visible())

    def test_sign_in_using_invalid_account(self):
        main_page = MainPage(self.driver)
        sign_in = SignInPage(self.driver)
        main_page.click_sign_in_button()
        sign_in.sign_in_using_invalid_account()
 #       assert. dodać sprawdzanie czy jest info there is error

    def test_sign_out(self):
        main_page = MainPage(self.driver)
        sign_in = SignInPage(self.driver)
        main_page.click_sign_in_button()
        sign_in.sign_in_using_valid_account()
        sign_in.sign_out()
        self.assertTrue(sign_in.check_is_sign_in_button_visible())
