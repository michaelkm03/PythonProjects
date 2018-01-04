from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest

class ScreenCapture(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_driver_path = '/Users/victorious/Desktop/Projects/Python Projects/PublicProjects/chromedriver'
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver_path)

    def test_Capture_URL(self):
        self.driver.get('https://www.linkedin.com/feed/')
        self.driver.get_screenshot_as_file("capture.png")

if __name__ == '__main__':
    unittest.main()