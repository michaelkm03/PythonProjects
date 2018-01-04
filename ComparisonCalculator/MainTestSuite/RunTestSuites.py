import unittest
from UnitTests import NumberTestCase

def ComparisonTestSuite():
    comparisonTest = unittest.TestSuite()
    comparisonTest.addTest(NumberTestCase("testOutOfBounds"))
    comparisonTest.addTest(NumberTestCase("testInBounds"))
    comparisonTest.addTest(NumberTestCase("testBoundsDynamically"))
    comparisonTest.addTest(NumberTestCase("testEnforcedDigitEntries"))
    return comparisonTest


if __name__ == '__main__':
    suite = ComparisonTestSuite()
    runner = unittest.TextTestRunner()
    runner.run(suite)