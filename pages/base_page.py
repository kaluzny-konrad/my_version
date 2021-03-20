from collections import namedtuple

Locator = namedtuple("Locator", ["by", "value"])
Url = namedtuple("Url", ["domain", "path"])

class BasePage():
    domain = None
    path = None
    
    def __init__(self, driver):
        self.driver = driver
        self.url = Url(self.domain, self.path)

    def go(self):
        self.driver.get(self.url.domain+'/'+self.url.path)
    