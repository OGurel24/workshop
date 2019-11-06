from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class MainPage:
    REGISTER_BUTTON = (By.CLASS_NAME, "StaticLoggedOutHomePage-buttonSignup")
    LOGIN_BUTTON = (By.CLASS_NAME, 'StaticLoggedOutHomePage-buttonLogin')

    def __init__(self, driver):
        """

        :param selenium.webdriver.chrome. driver:
        """
        self.driver = driver

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.LOGIN_BUTTON)).click()
        return LoginPage(self.driver)

    def click_register_button(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.REGISTER_BUTTON)).click()
        return RegisterPage(self.driver)


class LoginPage:
    EMAIL_INPUT = (By.CLASS_NAME, "js-username-field")
    PASSWORD_INPUT = (By.CLASS_NAME, 'js-password-field')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '#page-container > div > div.signin-wrapper > form > div.clearfix > button')

    def __init__(self, driver):
        """

        :param selenium.webdriver.chrome. driver:
        """
        self.driver = driver

    def fill_email_area(self, email):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.PASSWORD_INPUT)).send_keys(email)

    def fill_password_area(self, password):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.SUBMIT_BUTTON)).send_keys(password)

    def submit(self):
        WebDriverWait(self.driver, 10).until(ec.element_located_to_be_selected(self.SUBMIT_BUTTON)).click()


