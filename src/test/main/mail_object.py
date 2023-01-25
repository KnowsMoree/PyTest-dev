import main


class MailObject(main.TestWebsite):
    def input_username(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='username']")

    def input_password(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='password']")

    def submit_auth(self):
        return self.driver.find_element(self.by.XPATH, "//input[@type='submit']")

    def refresh(self):
        return self.driver.find_element(self.by.XPATH, "//div[@class='ImgRefreshAll']")

    def msg_list_1(self):
        return self.driver.find_element(self.by.XPATH, "/html/body/div[4]/div[10]/div[1]/table/tbody/tr[2]/td/ul/li[1]")

    def date_get(self):
        return self.driver.find_element(self.by.XPATH, "//td[contains(@class, 'DateCol')]")
