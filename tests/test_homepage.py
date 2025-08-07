import allure
from pages.home_page import HomePage

@allure.feature("Homepage")
@allure.story("Open Homepage")
@allure.title("User can open Insider homepage and see banner")
def test_homepage_load_and_verify_banner(driver):
    home_page = HomePage(driver)

    with allure.step("Load the homepage"):
        home_page.load()

    with allure.step("Verify banner is displayed"):
        assert home_page.is_banner_displayed(), "Banner not visible"

    with allure.step("Verify CTA banner is displayed"):
        assert home_page.is_cta_banner_displayed(), "CTA banner not visible"