from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_element import BaseElement

class BaseInput(BaseElement):
    element_type = 'input'

    def set(self, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator=self.locator)
        )
        element.clear()
        element.send_keys(text)
        return None

    @property
    def text(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator=self.locator)
        )
        txt = element.get_attribute("value")
        return txt