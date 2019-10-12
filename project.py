from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
#driver.get('https://www.meetup.com/TestHive')
driver.get('https://www.stackoverflow.com/')

element = driver.find_element_by_name('q')
element.send_keys("onur")
element.send_keys(Keys.ENTER)

sleep(3)

driver.close()



