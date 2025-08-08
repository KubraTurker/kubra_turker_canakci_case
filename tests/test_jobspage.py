import allure
from pages.jobs_page import JobsPage
from pages.lever_page import LeverPage


@allure.feature("QA Job Listings")
@allure.story("Filter QA Jobs by Location and Department")
@allure.title("User can filter QA jobs for Istanbul and verify Lever form redirection")
def test_qa_job_listings(driver):
    jobs_page = JobsPage(driver)

    with allure.step("Open the QA Careers Page and handle cookie banner if present"):
        jobs_page.load()
        jobs_page.handle_cookie()

    with allure.step("Click on the 'See all QA jobs' button to view the job listings"):
        jobs_page.click_see_all_qa_jobs()

    with allure.step("Apply filters: Location = 'Istanbul, Turkey' and Department = 'Quality Assurance'"):
        jobs_page.filter_by_location_and_department()

    with allure.step("Verify that all filtered job listings contain the expected Position, Department, and Location"):
        job_texts = jobs_page.get_all_job_details()

        assert len(job_texts) > 0, "No job listings found after applying filters."

        for job in job_texts:
            assert "Quality Assurance" in job, f"Position does not contain 'Quality Assurance': {job}"
            assert "Istanbul, Turkiye" in job, f"Location is not 'Istanbul, Turkiye': {job}"

    with allure.step("Hover over the first job card, scroll to 'View Role' button, click it and switch to new tab"):
        jobs_page.click_first_view_role()

    with allure.step("Verify that the redirection leads to the Lever Application Form page"):
        lever_page = LeverPage(driver)
        assert lever_page.is_on_lever_application_form(), \
            f"Expected Lever application form, but current URL is: {driver.current_url}"
