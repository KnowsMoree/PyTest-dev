import main


class TestReg(main.TestWebsite):
    def test_reg(self):
        link_create = self.browser.find_element(self.by.XPATH, "/html/body/div/div/div/div[1]/div[2]/div[1]/a[1]")
        link_create.click()
        main.delay(5)

    def test_reg_nik(self):
        link_create = self.browser.find_element(self.by.XPATH, "/html/body/div/div/div/div[1]/div[2]/div[1]/a[1]")
        link_create.click()
        uname = self.browser.find_element(self.by.XPATH, "//*[@id='idcard']")
        uname.send_keys("8928839489849203")
        main.delay(3)
