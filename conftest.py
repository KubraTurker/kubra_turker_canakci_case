import pytest
from selenium import webdriver
import tempfile

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")
    options.add_argument('--disable-notifications')

    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")


    temp_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={temp_dir}")


    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()