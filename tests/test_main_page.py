import unittest
from tests.base_test import BaseTest
from pages.main_page import *


class TestMainPage(BaseTest):

    def test_go_to_login_page(self):
        main_page = MainPage(self.driver)
        main_page.click_sign_in_button()
        self.assertTrue(main_page.check_is_create_account_button_visible())
