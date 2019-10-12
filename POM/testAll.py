import unittest
from selenium import webdriver
from POM.page import *
from POM.locators import *
from time import sleep


class TestPythonOrg(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()


class TestHome(TestPythonOrg):

    def setUp(self):
        super().setUp()
        self.home = HomePage(self.driver)

    def test_TC1(self):
        self.home.hover_to(CommonPageLocators.DOC)
        self.home.assert_elem_text(CommonPageLocators.PY3_DOC_BUTTON, 'Python 3.x Docs')
        self.home.click(CommonPageLocators.PY3_DOC_BUTTON)
        assert (self.driver.current_url == 'https://docs.python.org/3/')
        sleep(3)

    def test_TC2(self):
        self.home.search_for("blahbladlkdfjdfjıfjıdh")
        self.home.assert_elem_text(CommonPageLocators.SEARCH_RESULT_LIST, 'No results found.')
        sleep(1)


class TestAbout(TestPythonOrg):

    def setUp(self):
        super().setUp()
        self.about = AboutPage(self.driver)

    def test_TC3(self):
        self.about.wait_element(AboutPageLocators.UPCOMING_EVENTS)