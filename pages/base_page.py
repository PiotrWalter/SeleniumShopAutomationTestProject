from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage(object):
    def __init__(self, driver, base_url='http://automationpractice.com/index.php'):
        self.base_url = base_url
        self.driver = driver
        self.valid_user_login = 'piotrwaltrowski@gmail.com'
        self.valid_user_password = 'XJvF2@s3GeLx9L@'
        self.invalid_user_login = 'invalid'
        self.invalid_user_password = '1234'

    def element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((locator)))

    def presence_of_element_located(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locator)))

    def visibility_of_element_located(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((locator)))

    def find_one_element(self, locator):
        return self.driver.find_element_by_class_name(locator)
    # change using EC, also change name

    def find_all_elements(self, locator):
        return self.driver.find_elements_by_class_name(locator)
    # change using EC, also change name

