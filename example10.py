from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.events import *
import os


class MyListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print("Log: Before " + url)
    def after_navigate_to(self, url, driver):
        print("Log: After " + url)


driver = webdriver.Chrome()
ef_driver = EventFiringWebDriver(driver, MyListener())
html_file = os.getcwd() + "/34.html"
ef_driver.get("https://python.org")
driver.maximize_window()
sleep(3)
driver.close()
