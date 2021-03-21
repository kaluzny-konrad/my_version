from ..base_listing import BaseListing

class TrialStonesListing(BaseListing):

    locator = './/div/span/..'
    element_locators = {
        'name': './span/b',
        'wealth': './p'
    }

    @property
    def highest_wealth(self):
        return self.listings_df['wealth'].max()

    @property
    def highest_wealth_name(self):
        return self.listings_df.loc[
            self.listings_df['wealth']==self.listings_df['wealth'].max()
        , 'name'][0]