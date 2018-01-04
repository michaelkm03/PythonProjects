
class Endpoints:

    def __init__(self, driver):
        self.driver = driver

    def AllEndpoints(self):
        elements = self.driver.find_elements_by_tag_name('a')
        endpoints = {}

        # Find all enpoints and add to map
        for element in elements:
            endpoints[element.text] = element.get_attribute('href')

        return endpoints
import unittest
from selenium import webdriver
from General import Endpoints

class BaseCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/victorious/Desktop/Projects/AutomatedTesting/PublicProjects/chromedriver')
        self.driver.get("https://the-internet.herokuapp.com/")

    def test_ValidEnpoints(self):
        endpoints = Endpoints(self.driver).AllEndpoints()
        errors = {}
        # Navigate to each endpoint, assert True if endpoinr == current url
        for endpoint in endpoints:
            self.driver.get(endpoints[endpoint])
            # self.assertEqual((endpoints[endpoint]), self.driver.current_url)