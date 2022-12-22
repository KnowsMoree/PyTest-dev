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

    @pytest.fixture(autouse=True)
    def browser_setup_and_teardown(self):
        self.keys = Keys
        self.by = By
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

        self.browser.maximize_window()
        self.browser.implicitly_wait(10)
        self.browser.get("https://app.tandatanganku.com/")

        yield

        self.browser.close()
        self.browser.quit()
