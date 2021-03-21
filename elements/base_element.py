from selenium.common.exceptions import NoAlertPresentException, UnexpectedAlertPresentException
from pages.base_page import Locator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

class BaseElement():
    type_element = None

    def __init__(self, driver, by, value):
        self.driver = driver
        self.locator = Locator(by, value)
        self.web_element = None
        self.find()
    
    def find(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator=self.locator)
        )
        self.web_element = element
        return None

    def click(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator=self.locator)
        )
        element.click()
        try:
            print(Alert(self.driver).text)
            Alert(self.driver).accept()
        except NoAlertPresentException:
            pass
        return None