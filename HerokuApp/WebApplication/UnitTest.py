import unittest
from selenium import webdriver
from General import Endpoints
from BaseTest import BaseCase

class UnitTest(BaseCase.setUp(unittest.TestCase)):

    def words(self):
        print "made it"

if __name__ == '__main__':
    unittest.main()