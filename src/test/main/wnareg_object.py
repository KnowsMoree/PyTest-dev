import main


class WnaregObject(main.TestWebsite):
    def link_reg_wna(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='menubar']/div/div/div/a[2]")

    def link_reg(self):
        return self.driver.find_element(self.by.XPATH, "/html/body/div/div/div/div[1]/div[2]/div[1]/a[1]")

    def verification_method(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='metode_verifikasi']")

    def number_kitas_input(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='kitas']")

    def number_passport_input(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='passport']")

    def name_input(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='fullname']")

    def birth_input(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='lbrith']")

    def national_input(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='nationality']")

    def select_gender(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='gender']")

    def select_day(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='Day']")

    def select_month(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='Month']")

    def select_year(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='Year']")

    def email_input(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='email']")

    def handphone_number_input(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='handphone']")

    def kitas_registered(self):
        return self.driver.find_element(
            self.by.XPATH, "//*[@id='e_kitas']")

    def passport_registered(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='e_passport']")

    def kitap_passport_same(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='e_passport']")

    def dropdown_method(self):
        return self.driver.find_element(self.by.id.metode_verifikasi, value='option')

    def button_next(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='step-1']/div[9]/button")

