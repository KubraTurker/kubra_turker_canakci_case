import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--disable-notifications')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()