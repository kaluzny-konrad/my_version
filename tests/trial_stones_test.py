from .base_test import BaseTest
from pages.tech_step_academy.trial_stones_page import TrialStonesPage

class TrialStonesPageTest(BaseTest):
    page_class = TrialStonesPage

    def __init__(self):
        super().__init__()
        print('-------------------------------------------------------')
        print(f'Test on site "{self.page_class.__name__}" has started.')
        self.set_correct_inputs()
        self.complete_tasks()
        self.run_assert_tests()
        self.end_test()
        print('-------------------------------------------------------\n')

    def set_correct_inputs(self):
        self.input1_answer = 'rock'
        self.correct_answer1 = 'Success!'
        self.correct_answer2 = 'Trial Complete'
    
    def complete_tasks(self):
        self.page.go()
        self.page.input1.set(self.input1_answer)
        self.page.button1.click()
        self.input2_answer = self.page.button1_answer
        self.page.input2.set(self.input2_answer)
        self.page.button2.click()
        self.input3_answer = self.page.listing_merchants.highest_wealth_name
        self.page.input3.set(self.input3_answer)
        self.page.button3.click()
        self.page.button4.click()

    def run_assert_tests(self):
        self.assert_test(self.page.input1.text, self.input1_answer)
        self.assert_test(self.page.input2.text, self.input2_answer)
        self.assert_test(self.page.input3.text, self.input3_answer)
        self.assert_test(self.page.button1_answer, self.input2_answer)
        self.assert_test(self.page.button2_answer, self.correct_answer1)
        self.assert_test(self.page.button3_answer, self.correct_answer1)
        self.assert_test(self.page.button4_answer, self.correct_answer2)