from bases.base_driver import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    URL = "https://useinsider.com/"

    BANNER_LOCATOR = (By.CSS_SELECTOR, "div[class*='hero']")
    HOMEPAGE_CTA_BANNER = (By.ID, "home-cta-banner")
    COMPANY_MENU = (By.LINK_TEXT,"Company")
    CAREERS_LINK = (By.LINK_TEXT, "Careers")

    def load(self):
        self.open(self.URL)
        self.wait_for_element(self.BANNER_LOCATOR)

    def is_banner_displayed(self):
        return self.driver.find_element(*self.BANNER_LOCATOR).is_displayed()

    def is_cta_banner_displayed(self):
        try:
            return self.driver.find_element(*self.HOMEPAGE_CTA_BANNER).is_displayed()
        except:
            return False

    def navigate_to_careers(self):
        self.wait_for_clickable(self.COMPANY_MENU).click()
        self.wait_for_clickable(self.CAREERS_LINK).click()
