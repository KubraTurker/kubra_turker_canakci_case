import time

from bases.base_driver import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class JobsPage(BasePage):

    URL = "https://useinsider.com/careers/quality-assurance/"

    TITLE_LOCATOR = (By.XPATH, "//h1[contains(text(),'Quality Assurance')]")
    SEE_ALL_QA_JOBS_BTN = (By.XPATH, "//a[contains(text(),'See all QA jobs')]")
    LOCATION_FILTER = (By.CLASS_NAME,"select2-container")
    DEPARTMENT_FILTER = (By.CSS_SELECTOR, "select[name='filter-by-department']")
    JOB_LIST = (By.CSS_SELECTOR, "div.position-list-item")
    FILTER_LOCATION = (By.XPATH, "//li[contains(text(),'Istanbul, Turkiye')]")
    VIEW_ROLE_BTN = (By.XPATH, ".//a[contains(text(),'View Role')]")
    JOB_CARD = (By.CSS_SELECTOR, "div.position-list-item, a.position-list-item")

    def load(self):
        self.driver.get(self.URL)
        self.wait_for_element(self.TITLE_LOCATOR)

    def click_see_all_qa_jobs(self):
        self.wait_for_element(self.SEE_ALL_QA_JOBS_BTN).click()

    def filter_by_location_and_department(self):

        while 1:
            result_count = self.driver.find_element(By.CLASS_NAME, 'totalResult')
            if result_count.text != "":
                total_count = result_count.text
                break

            time.sleep(1)

        self.scroll_to_element(self.LOCATION_FILTER).click()
        self.wait_for_element(self.FILTER_LOCATION).click()

        while 1:
            result_count = self.driver.find_element(By.CLASS_NAME, 'totalResult')
            if result_count.text != total_count:
                break

            time.sleep(1)


    def get_job_listings(self):
        return self.wait_for_elements(self.JOB_LIST)

    def get_all_job_details(self):
        jobs = self.get_job_listings()
        return [job.text for job in jobs]


    def get_job_cards(self):
        return self.wait_for_elements(self.JOB_CARD)


    def click_first_view_role(self):
        job_cards = self.get_job_cards()

        if not job_cards:
            raise AssertionError("No job cards available to click 'View Role'.")

        first_card = job_cards[0]

        ActionChains(self.driver).move_to_element(first_card).perform()

        self.scroll_to_element(self.VIEW_ROLE_BTN)

        handles_before = set(self.driver.window_handles)

        self.wait.until(EC.element_to_be_clickable(self.VIEW_ROLE_BTN)).click()

        self.wait.until(
            lambda d: len(d.window_handles) > len(handles_before)
        )

        new_handles = set(self.driver.window_handles) - handles_before
        if new_handles:
            self.driver.switch_to.window(new_handles.pop())
