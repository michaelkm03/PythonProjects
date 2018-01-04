from selenium.webdriver.common.by import By

class numberGenerator:

    def __init__(self, driver):
      self.driver = driver

    def compare(self, compare, n1, n2):
        '''
        :param: Object (self);  compare, n1, n2 (Integers)

            Determine if compare is between n1 and n2 values

        :return: Boolean
        '''

        if ((compare > n1 and compare < n2) or (compare < n1 and compare > n2)):
            return True
        else:
            return False

    def findAndSetValues(self, num1, num2, compare):
        '''
       :params:  n1, n2, compare (Integers)

                Using webdriver, locate three fields on app and set parameters (n1, n2, compare)

        :return: None
         '''
        self.driver.find_element_by_name("numFirst").send_keys(num1)
        self.driver.find_element_by_name("numSecond").send_keys(num2)
        self.driver.find_element_by_name("numToCompare").send_keys(compare)

    def submit(self):
        '''
        :param: Object
                Using webdriver, located submit button by xpath and click.  Log response in 'response' obj for later use
        :return: response obj
        '''
        self.driver.find_element_by_xpath(xpath='//*[@id="app"]/div/div/form/input').click()

    def getAlerts(self):
        '''
        :param: Object
                Get alerts from class name 'alert-danger';  if present, appends it to alerts list
        :return: alerts list
        '''

        alerts = []
        alertElements = self.driver.find_elements(By.CLASS_NAME, "alert-danger")
        for el in alertElements:
          alerts.append(el.text)
        return alerts

    def checkForInputNAlert(self, n):
        '''
        :param: Object

            Get alerts from class name 'alert-danger' and appends to list.

        :return: alerts list
        '''

        alertPrefix = "N/A"
        if n == 1:
          alertPrefix = "First number"
        if n == 2:
          alertPrefix = "Second number"
        if n == 3:
          alertPrefix = "Number to compare"

        alerts = self.getAlerts()

        for alert in alerts:
          if alertPrefix in alert:
            return True
        return False

    def results(self):
        '''
        :param: Object

            Determines if 'is not between' is in text response, mark True;  Else, mark False

        :return: application response
        '''
        response = self.driver.find_element(By.CLASS_NAME, "modal-body").text
        if "is not between" in response:
            actual = False
        else:
            actual = True
        return actual