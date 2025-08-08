import allure

from pages.home_page import HomePage
from pages.careers_page import CareersPage

@allure.feature("Homepage")
@allure.story("Open Homepage")
@allure.title("User can open Insider homepage and see banner")
def homepage_load_and_verify_banner(driver):
    home_page = HomePage(driver)

    with allure.step("Load the homepage"):
        home_page.load()

    with allure.step("Verify banner is displayed"):
        assert home_page.is_banner_displayed(), "Banner not visible"

    with allure.step("Verify CTA banner is displayed"):
        assert home_page.is_cta_banner_displayed(), "CTA banner not visible"

@allure.feature("Careers Page")
@allure.story("Verify key sections are visible")
@allure.title("User can see Locations, Teams, and Life at Insider sections")
def career_page_blocks(driver):
    home_page = HomePage(driver)

    with allure.step("Handle cookie banner if visible"):
        home_page.handle_cookie()

    with allure.step("Navigate to the Careers page via menu"):
        home_page.navigate_to_careers()

    careers_page = CareersPage(driver)

    with allure.step("Verify 'Our Locations' section is visible"):
        assert careers_page.is_locations_visible(), "Locations block not visible"

    with allure.step("Verify 'Find Your Calling' section is visible"):
        assert careers_page.is_teams_visible(), "Teams block not visible"

    with allure.step("Verify 'Life at Insider' section is visible"):
        assert careers_page.is_life_at_insider_visible(), "Life at Insider block not visible"


@allure.feature("Homepage and Careers Flow")
@allure.story("Full navigation from Homepage to Careers")
@allure.title("User can open Homepage and verify Careers page sections")
def test_flow(driver):
    with allure.step("Step 1: Verify Homepage banners"):
        homepage_load_and_verify_banner(driver)

    with allure.step("Step 2: Verify Careers page key sections"):
        career_page_blocks(driver)
