import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class MySeleniumTest(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    self.driver.maximize_window()
    self.driver.get("https://www.example.com")

  def tearDown(self):
    self.driver.quit()

  def test_page_title(self):
    self.assertEqual("Example Domain", self.driver.title)

  def test_find_element(self):
    element = self.driver.find_element("link text", "More information...")
    self.assertIsNotNone(element)

if __name__ == '__main__':
  unittest.main()