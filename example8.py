from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://python.org")
sleep(1)
driver.get("https://google.com")
sleep(1)

driver.back()
sleep(1)
driver.forward()
sleep(1)
driver.refresh()
sleep(1)
driver.quit()