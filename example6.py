from selenium import webdriver
import os
from time import sleep

driver = webdriver.Chrome()
html_file = os.getcwd() + "/onur.html"
driver.maximize_window()
driver.get("file:///" + html_file)

try:
    assert "Your file was not found" not in driver.page_source
except AssertionError:
    print("Error")

#print(driver.page_source)

driver.quit()