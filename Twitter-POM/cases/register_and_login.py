import unittest
from pages.pages import MainPage
from selenium import webdriver
import time


class TwitterTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://twitter.com")
        self.main_page = MainPage(self.driver)

    def test_login(self):
        login_page = self.main_page.click_login_button()
        login_page.fill_email_area(email='onr_gurel')
        login_page.fill_password_area(password='wrong pass')
        login_page.submit()
        time.sleep(3)

    @unittest.skip("Time!!!")
    def test_register(self):
        register_page = self.main_page.click_register_button()
        login_page.fill_email_area(email='onr_gurel')
        login_page.fill_password_area(password='wrong pass')
        login_page.submit()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
