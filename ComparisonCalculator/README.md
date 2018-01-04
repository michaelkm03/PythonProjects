# NuOrder Comparison Calculator

## Web Application
- Download selen_prob folder
- cd into the root folder, run npm install, then run npm start

## Dependencies
- the latest Selenium download
- ensure you have a chrome.exe driver file download.  Then, modify the path to the .exe file in UnitTests/SetUp()

## How to Run Tests
- clone repo https://github.com/michaelkm03/PublicProjects
- cd to MainTestSuite and run desired test.py file

## Files
- UnitTests.py
-- Contains Test Object constructor (setup(), which is automatically called when instantiated) and all individual unit tests 
-- Running UnitTests.py file will excecute all UnitTest found in class 'CompareTestCase' whose function starts with 'test'
(e.g, Run UnitTests.py >>> all tests run EXCEPT 'setManual')
-- Each test contains assertion

## Functions.py
class GenerateTestData: contains three functions
1. generate random set of integers 
2. random string of characters 
3. comparision function to determine if value is between two others 

class AppCommand: contains three functions
1. find fields to set values and sets them
2. find button to submit and clicks 'submit' (returns response obj)
3. determine answer of web application after submit click

## RunTestSuites.py
- contains single function that takes no paramaters and creates an instance of unittest.TestSuite()
- use function 'addtest' to add single test to TestSuite obj (pass name of test as string)
- use function 'addtests' to add an iterable of one or more tests 
- run this file as 'RunTestSuites.py' to excecute collection of tests

## Output
- Browser should open for every test run and navigate to web application
- Verbosity is set to display basic results of tests
