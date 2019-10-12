from selenium import webdriver
import os
from time import sleep

driver = webdriver.Chrome()
html_file = os.getcwd() + "/25_radio_buttons.html"
driver.maximize_window()
driver.get("file:///" + html_file)

sleep(2)
driver.execute_script("document.body.style.zoom = '1.5'")
sleep(2)

elements = driver.find_elements_by_css_selector('input')
elements[0].click()
sleep(2)
elements[2].click()

for button in buttons:
    print('Button: {}, Checked: {}'.format(button.get_attribute('value'), button.get_attribute('checked')))