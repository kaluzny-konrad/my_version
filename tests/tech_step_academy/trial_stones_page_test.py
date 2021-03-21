import browsers
import terminal
from pages.tech_step_academy.trial_stones_page import TrialStonesPage

if __name__ == '__main__':

    # Clear terminal
    terminal.cls()

    # Automate
    browser = browsers.get_chrome()
    assert browser != None, f'Webdriver error.'
    page = TrialStonesPage(browser)
    page.go()
    input1_answer = 'rock'
    page.input1.set(input1_answer)
    page.button1.click()
    input2_answer = page.button1_answer
    page.input2.set(input2_answer)
    page.button2.click()
    input3_answer = page.listing_merchants.highest_wealth_name
    page.input3.set(input3_answer)
    page.button3.click()
    page.button4.click()

    # Test
    assert page.input1.text == input1_answer, (
        f'Get: {page.input1.text} | Set: {input1_answer}')

    assert page.input2.text == input2_answer, (
        f'Get: {page.input2.text} | Set: {input2_answer}')

    assert page.input3.text == input3_answer, (
        f'Get: {page.input3.text} | Set: {input3_answer}')

    assert page.button1_answer == input2_answer, (
        f'Get: {page.button1_answer} | Set: {input2_answer}')


    correct_answer1 = 'Success!'

    assert page.button2_answer == correct_answer1, (
        f'Get: {page.button2_answer} | Set: {correct_answer1}')

    assert page.button3_answer == correct_answer1, (
        f'Get: {page.button3_answer} | Set: {correct_answer1}')


    correct_answer2 = 'Trial Complete'

    assert page.button4_answer == correct_answer2, (
        f'Get: {page.button4_answer} | Set: {correct_answer2}')