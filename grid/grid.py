# create hub
# java -jar seleni... -role hub
# create node
# java -jar selenium-ser... -role node -hub ....
from selenium import webdriver
import time

driver = webdriver.Remote(command_executor='http://192.168.3.14:4444/wd/hub',
                          desired_capabilities={'browserName': 'chrome'})

time.sleep(100)
driver.close()
