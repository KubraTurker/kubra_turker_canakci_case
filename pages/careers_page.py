from bases.base_driver import BasePage
from selenium.webdriver.common.by import By


class CareersPage(BasePage):

    LOCATIONS_BLOCK = (By.XPATH, "//h3[contains(text(),'Our Locations')]")
    TEAMS_BLOCK = (By.XPATH, "//h3[contains(text(),'Find your calling')]")
    LIFE_AT_INSIDER_BLOCK = (By.XPATH, "//h2[contains(text(),'Life at Insider')]")

    def is_locations_visible(self):
        try:
            return self.wait_for_element(self.LOCATIONS_BLOCK).is_displayed()
        except:
            return False

    def is_teams_visible(self):
        try:
            return self.wait_for_element(self.TEAMS_BLOCK).is_displayed()
        except:
            return False

    def is_life_at_insider_visible(self):
        try:
            return self.scroll_to_element(self.LIFE_AT_INSIDER_BLOCK).is_displayed()
        except:
            return False

