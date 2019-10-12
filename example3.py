from selenium import webdriver
import os
from time import sleep

driver = webdriver.Chrome()
html_file = os.getcwd() + "/24_clickable_dropdown.html"
driver.maximize_window()
driver.get("file:///" + html_file)

dropdown = driver.find_element_by_css_selector('body > div > button')
dropdown.click()
sleep(2)
about = driver.find_element_by_css_selector('#myDropdown > a:nth-child(2)')
about.click()