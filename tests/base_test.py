import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):
    driver = webdriver.Chrome(r"C:\python_projects\chromedriver.exe")
    driver.maximize_window()

    def setUp(self):
        # opening browser
        self.driver.get("http://automationpractice.com/index.php")

    # def tearDown(self):
    #    self.driver.quit()
