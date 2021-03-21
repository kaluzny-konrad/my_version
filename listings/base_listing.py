from lxml import etree
import pandas as pd

class BaseListing:

    locator = None
    element_locators = None

    def __init__(self, driver):
        html = driver.page_source
        self.tree = etree.HTML(html)

    def get_listings_df(self):
        listings = self.tree.findall(self.locator)
        df = pd.DataFrame([])
        for listing in listings:
            df = df.append(self.get_elements_df(listing), ignore_index=True)
        return df

    def get_elements_df(self, listings):
        columns = []
        data = []
        for element in self.element_locators:
            columns.append(element)
            data.append(listings.find(self.element_locators[element]).text)
        return pd.DataFrame([data], columns=columns)

    @property
    def listings_df(self):
        return self.get_listings_df()