import unittest
from selenium import webdriver
from POM.page import *
from POM.locators import *
from time import sleep


class TestPythonOrg(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


class TestHome(TestPythonOrg):

    def setUp(self):
        super().setUp()
        self.home = HomePage(self.driver)

    @unittest.skip("")
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


    def test_TC4(self):
        self.assertEqual(self.home.driver.title, "Welcome to Python.org", "ERROR")


class TestAbout(TestPythonOrg):

    def setUp(self):
        super().setUp()
        self.about = AboutPage(self.driver)

    @unittest.skip("")
    def test_TC3(self):
        self.about.wait_element(AboutPageLocators.UPCOMING_EVENTS)

    @unittest.skip("")
    def test_TC5(self):
        self.assertIn('about', self.about.driver.current_url)
        self.assertTrue('about' in self.about.driver.current_url)
