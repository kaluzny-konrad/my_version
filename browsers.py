from selenium import webdriver

def get_chrome_browser():
    return webdriver.Chrome('C:\projects\drivers\chromedriver.exe')

def get_edge_browser():
    return webdriver.Edge('C:\projects\drivers\msedgedriver.exe')