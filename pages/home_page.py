from bases.base_driver import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    URL = "https://useinsider.com/"

    _banner_locator = (By.CSS_SELECTOR, "div[class*='hero']")
    _homepage_cta_banner = (By.ID, "home-cta-banner")

    def load(self):
        self.open(self.URL)
        self.wait_for_element(self._banner_locator)

    def is_banner_displayed(self):
        return self.driver.find_element(*self._banner_locator).is_displayed()

    def is_cta_banner_displayed(self):
        try:
            return self.driver.find_element(*self._homepage_cta_banner).is_displayed()
        except:
            return False
