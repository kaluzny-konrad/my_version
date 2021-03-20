from pages.tech_step_academy.training_ground import TrainingGround
from browsers import get_chrome_browser
from pages.tech_step_academy.main_page import TsaMainPage
from pages.tech_step_academy.trial_of_the_stones import TsaTrialStones

browser = get_chrome_browser()
page = TsaTrialStones(browser)
page.go()
page = TrainingGround(browser)
page.go()
print(page.button1.text)
page.button1.click()
