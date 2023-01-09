import time
import pyautogui
import pytest
import datetime

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# delay
def delay(sec):
    time.sleep(sec)


# choose web browser
def driver_manager(driver):
    if driver is "chrome":
        return webdriver.Chrome(ChromeDriverManager().install())
    elif driver is "firefox":
        return webdriver.Firefox()


class TestWebsite:
    # web browser used to test
    driver = driver_manager("chrome")

    # url to test
    url = {
        "prod": "https://app.digisign.id",
        "test": "https://app.tandatanganku.com"
    }

    # setup test
    @pytest.fixture(autouse=True)
    def browser_setup_and_teardown(self):
        self.keys = Keys
        self.by = By
        self.robot = pyautogui

        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.delete_all_cookies()

        self.driver.get(self.url["prod"])

        self.actions = ActionChains(self.driver)

        yield
