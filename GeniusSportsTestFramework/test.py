import unittest
import time
import calendar
from selenium import webdriver

class BaseCase(unittest.TestCase):

    def test_getSports(self):
        self.driver = webdriver.Chrome('/Users/victorious/Desktop/Projects/Python Projects/PublicProjects/GeniusSportsTestFramework/chromedriver')
        self.driver.get('https://opap.betstream.betgenius.com/betstream-view/page/opapgeniusbetexternaltest/desktop/home')
        if (self.driver.current_url == 'https://opap.betstream.betgenius.com/betstream-view/page/opapgeniusbetexternaltest/desktop/home'):
            tree_nav = self.driver.find_elements_by_class_name('ui-sportsbook-navigation-Tree')
            sports_nav = []
            endpoint_map = {}
            for sport in tree_nav:
                sport = sport.text
                sports_nav.append(sport)
                endpoint_map[sport] = 'sport?sportId=%s&culture=' % (str(sport).upper())

        print '### ENDPOINTS ###'
        for key in endpoint_map:
            print '| ' + key + '  |'# + endpoint_map[key] + '  |'


if __name__ == '__main__':
    unittest.main()