from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException

def get_chrome():
    browser = None
    try:
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        browser = webdriver.Chrome(options=options,
            executable_path='C:\projects\drivers\chromedriver.exe')
    except SessionNotCreatedException:
        print('Webdriver error. Download correct version of driver.')
    return browser

def get_edge():
    browser = None
    try:
        browser = webdriver.Edge('C:\projects\drivers\msedgedriver.exe')
    except SessionNotCreatedException:
        print('Webdriver error. Download correct version of driver.')
    return browser