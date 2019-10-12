from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://python.org")

sleep(2)
driver.execute_script("document.body.style.zoom = '1.5'")
sleep(2)

# explicit wait
elem = WebDriverWait (driver, 10).until(EC.presence_of_element_located((By.ID, "about")))
driver.save_screenshot("SS/ss.png")

driver.quit()
