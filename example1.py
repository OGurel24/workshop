# Test Case description
# 1. Open a browser
# 2. Go to python.org
# 3. Web page title contains word python

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://python.org')
assert 'fdf' in driver.title.lower()
# driver.execute_script("document.body.style.zoom = '1' ")
driver.quit()
