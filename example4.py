from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
html_file = os.getcwd() + "/24_hoverable_dropdown.html"
driver.maximize_window()
driver.get("file:///" + html_file)

elem = driver.find_element_by_css_selector('body > div > span')
ActionChains(driver).move_to_element(elem).perform()
sleep(2)

elem_hello_world = driver.find_element_by_css_selector(body > div > div > p)
print(elem_hello_world.text)