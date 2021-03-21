from .base_element import BaseElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseText(BaseElement):
    element_type = 'text'

    @property
    def text(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator=self.locator)
        )
        txt = element.text
        return txt