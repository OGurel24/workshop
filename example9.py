from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
html_file = os.getcwd() + "/33.html"
driver.maximize_window()
driver.get("file:///" + html_file)

driver.find_element_by_css_selector('body > button').click()
sleep(1)

driver.switch_to.alert.accept()
sleep(2)

driver.find_element_by_css_selector('body > button').click()
sleep(1)

driver.switch_to.alert.dismiss()
sleep(2)


driver.close()