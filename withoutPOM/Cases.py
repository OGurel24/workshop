import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys


class TestPythonOrg(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://python.org')

    def test_3(self):
        about = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#about > a')))
        about.click()
        self.assertTrue(EC.presence_of_element_located((By.CSS_SELECTOR,
             '#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul')))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
