from selenium.webdriver.common.by import By

from .main_page import MainPage

from elements.base_input import BaseInput
from elements.base_button import BaseButton
from elements.base_select import BaseSelect
from elements.base_text import BaseText


class TrainingGroundPage(MainPage):
    path = "training-ground"

    @property
    def button1(self):
        return BaseButton(self.driver, by=By.CSS_SELECTOR, value="button#b1")

    @property
    def button2(self):
        return BaseButton(self.driver, by=By.CSS_SELECTOR, value="button#b2")

    @property
    def button3(self):
        return BaseButton(self.driver, by=By.CSS_SELECTOR, value="button#b3")

    @property
    def button4(self):
        return BaseButton(self.driver, by=By.CSS_SELECTOR, value="button#b4")

    @property
    def input1(self):
        return BaseInput(self.driver, by=By.CSS_SELECTOR, value="input#ipt1")

    @property
    def input2(self):
        return BaseInput(self.driver, by=By.CSS_SELECTOR, value="input#ipt2")

    @property
    def select1(self):
        return BaseSelect(self.driver, by=By.CSS_SELECTOR, value="select#ipt2")