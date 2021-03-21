from selenium.webdriver.common.by import By

from .main_page import MainPage

from elements.base_input import BaseInput
from elements.base_button import BaseButton
from elements.base_select import BaseSelect
from elements.base_text import BaseText

from listings.tech_step_academy.trial_stones_listing import TrialStonesListing

class TrialStonesPage(MainPage):
    path = "trial-of-the-stones"

    @property
    def input1(self):
        return BaseInput(self.driver, 
            by=By.CSS_SELECTOR, value="input#r1Input")

    @property
    def input2(self):
        return BaseInput(self.driver, 
            by=By.CSS_SELECTOR, value="input#r2Input")

    @property
    def input3(self):
        return BaseInput(self.driver, 
            by=By.CSS_SELECTOR, value="input#r3Input")

    @property
    def button1(self):
        return BaseButton(self.driver, 
            by=By.CSS_SELECTOR, value="button#r1Btn")

    @property
    def button1_answer(self):
        return BaseText(self.driver, 
            by=By.CSS_SELECTOR, value="div#passwordBanner").text

    @property
    def button2(self):
        return BaseButton(self.driver, 
            by=By.CSS_SELECTOR, value="button#r2Butn")

    @property
    def button2_answer(self):
        return BaseText(self.driver, 
            by=By.CSS_SELECTOR, value="div#successBanner1").text

    @property
    def button3(self):
        return BaseButton(self.driver, 
            by=By.CSS_SELECTOR, value="button#r3Butn")

    @property
    def button3_answer(self):
        return BaseText(self.driver, 
            by=By.CSS_SELECTOR, value="div#successBanner2").text

    @property
    def button4(self):
        return BaseButton(self.driver, 
            by=By.CSS_SELECTOR, value="button#checkButn")

    @property
    def button4_answer(self):
        return BaseText(self.driver, 
            by=By.CSS_SELECTOR, value="div#trialCompleteBanner").text

    @property
    def listing_merchants(self):
        return TrialStonesListing(self.driver)