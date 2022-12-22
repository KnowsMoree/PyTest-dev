#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def delay(sec):
    time.sleep(sec)


class TestWebsite:
    # 1. Check browser configuration in browser_setup_and_teardown
    # 2. Run 'Selenium Tests' configuration
    # 3. Test report will be created in reports/ directory
    driver = webdriver.Chrome(ChromeDriverManager().install())

    @pytest.fixture(autouse=True)
    def browser_setup_and_teardown(self):
        self.browser = self.driver
        self.keys = Keys

        self.browser.maximize_window()
        self.browser.implicitly_wait(10)
        self.browser.get("https://app.tandatanganku.com/")

        yield

        self.browser.close()
        self.browser.quit()

    def reg_object(self, element):
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
