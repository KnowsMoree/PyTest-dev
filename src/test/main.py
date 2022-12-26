import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def delay(sec):
    time.sleep(sec)


class TestWebsite:
    driver = webdriver.Chrome(ChromeDriverManager().install())

    @pytest.fixture(autouse=True)
    def browser_setup_and_teardown(self):
        self.keys = Keys

        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

        self.driver.get("https://app.digisign.id/")

        yield

        self.driver.close()
        self.driver.quit()

    def reg_and_log_object(self, element):
        match element:
            case "link_reg":
                return self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div[1]/a[1]")
            case "nik_input":
                return self.driver.find_element(By.XPATH, "//*[@id='idcard']")
            case "uname":
                return self.driver.find_element(By.XPATH, "//*[@id='username']")
            case "password":
                return self.driver.find_element(By.XPATH, "//input[@id='pd']")
            case "doc_file":
                return self.driver.find_element(By.XPATH, "//input[@type='file']")
            case "doc_submit":
                return self.driver.find_element(By.XPATH, "//button[@type='submit']")
            case "saldo_sign":
                return self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[11]/div[3]/div/div/div")
            case "password_salah":
                return self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger']")
            case "error_username":
                return self.driver.find_element(By.XPATH, "//*[@id='e_username']")
            case "pass_error":
                return self.driver.find_element(
                    By.XPATH, "//*[text() = '[Password salah sebanyak 3x. Silakan coba kembali setelah 10 menit.]']")

    def document_object(self, element):
        match element:
            case "need_sign":
                return self.driver.find_element(By.XPATH, "//a[contains(@href, 'needsign')]")
