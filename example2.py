from selenium import webdriver
import os
from time import sleep

driver = webdriver.Chrome()
html_file = os.getcwd() + "/23.html"
driver.maximize_window()
driver.get("file:///" + html_file)

sleep(3)
elem = driver.find_element_by_css_selector('body > form:nth-child(1) > input[type=checkbox]:nth-child(1)')
elem.click()

button = driver.find_element_by_css_selector('#disabled_button')
button.click()
print(button.is_enabled())

button2 = driver.find_element_by_css_selector('body > button:nth-child(4)')
print(button2.is_enabled())

text_field = driver.find_element_by_css_selector('body > form:nth-child(11) > input[type=text]:nth-child(8)')
text_field.send_keys("onur")
sleep(2)
text_field.clear()
sleep(2)

driver.quit()
