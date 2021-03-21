import os
from browser import base_browser

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class BaseTest():
    browser = base_browser.get_chrome()
    page_class = None
    sum_of_errors = 0

    def __init__(self):
        cls()
        try:
            self.page = self.page_class(self.browser)
        except:
            self.assert_test_not(self.browser, None)

    def assert_test(self, left, right):
        try:
            assert left == right, f'Get: {left} || Want: {right}'
        except AssertionError:
            self.sum_of_errors += 1

    def assert_test_not(self, left, right):
        try:
            assert left != right, f'Get: {left} || Want not: {right}'
        except AssertionError:
            self.sum_of_errors += 1

    def end_test(self):
        self.browser.quit()
        print(f'Sum of errors: {self.sum_of_errors}')