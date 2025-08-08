from bases.base_driver import BasePage
from selenium.webdriver.support import expected_conditions as EC


class LeverPage(BasePage):
    def is_on_lever_application_form(self) -> bool:
        self.wait.until(EC.url_matches(r".*lever\.co.*"))

        return "lever.co" in self.driver.current_url.lower()
