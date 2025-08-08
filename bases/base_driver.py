from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    COOKIE_DECLINE = (By.ID, "wt-cli-reject-btn")

    def __init__(self, driver, timeout=10):
        self.driver: webdriver.Chrome = driver
        self.wait: WebDriverWait = WebDriverWait(self.driver, timeout)


    def open(self, url):
        self.driver.get(url)

    def wait_for_element(self, locator) -> WebElement:
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator) -> WebElement:
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_elements(self, locator) -> [WebElement]:
        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )

    def scroll_to_element(self, locator) -> WebElement:
        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({ behavior: 'instant', block: 'center' });",
            element
        )

        return self.wait_for_element(locator)

    def handle_cookie(self):
        try:
            self.wait_for_element(self.COOKIE_DECLINE).click()
        except:
            print("Cookie decline button not found or already closed.")

