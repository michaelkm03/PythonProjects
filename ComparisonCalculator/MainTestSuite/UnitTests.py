import unittest
import random
import Functions as Functions
from selenium import webdriver

class NumberTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('PATH TO CHROME DRIVER')
        self.driver.get("http://localhost:3000/")
        self.numberGenerator = Functions.numberGenerator(self.driver)


    def testOutOfBounds(self):
        '''
        :param: Object (self)

            Set values num1, num2, compare in application and click submit.
            Values are in bounds and application should respond with "is not between"

        :return: Boolean
        '''
        n1 = 1
        n2 = 5
        c =  6

        # Set values and click submit
        self.numberGenerator.findAndSetValues(n1,n2,c)
        self.numberGenerator.submit()

        # Compare and assert pass
        actual = self.numberGenerator.results()
        self.assertFalse(actual)
        #Make sure alerts don't come up for valid entries
        self.assertFalse(self.numberGenerator.getAlerts())


    def testInBounds(self):
        '''
        :param: Object (self)

            Set values num1, num2, compare in application and click submit.
            Values are in bounds and application should respond with "is between"

        :return: Boolean
        '''
        n1 = 1
        n2 = 5
        c =  3

        # Set values and click submit
        self.numberGenerator.findAndSetValues(n1,n2,c)
        self.numberGenerator.submit()

        # Compare and assert pass
        actual = self.numberGenerator.results()
        self.assertTrue(actual)

    def testBoundsDynamically(self):
        '''
        :param: Object (self)

            Generate three random integers between 1 - 99, find/set values, get response.

        :return: Boolean
        '''
        n1 = random.randint(1, 99)
        n2 = random.randint(1, 99)
        c =  random.randint(1, 99)

        # Set values and click submit
        self.numberGenerator.findAndSetValues(n1,n2,c)
        self.numberGenerator.submit()

        # Compare and assert pass
        expected = self.numberGenerator.compare(c, n1, n2)
        actual = self.numberGenerator.results()
        self.assertTrue(expected == actual)

    def testEnforcedDigitEntries(self):
        '''
        :param: Object (self)

            Set bad entries and assert that error alerts are returned
            (Non empty alerts list is True, else empty is False

        :return: None
        '''
        n1 = "bad"
        n2 = "text"
        c = "entry"

        self.numberGenerator.findAndSetValues(n1,n2,c)
        self.numberGenerator.submit()

        alertOnePresent = self.numberGenerator.checkForInputNAlert(1)
        alertTwoPresent = self.numberGenerator.checkForInputNAlert(2)
        alertThreePresent = self.numberGenerator.checkForInputNAlert(3)

        self.assertTrue(alertOnePresent)
        self.assertTrue(alertTwoPresent)
        self.assertTrue(alertThreePresent)

if __name__ == '__main__':
    unittest.main()