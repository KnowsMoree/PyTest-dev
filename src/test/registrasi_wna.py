from main import WnaregObject, delay
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class TestwnaregObject(WnaregObject):
    def test_regwna_page(self):
        self.link_reg().click()
        self.link_reg_wna().click()
        delay(3)

    def test_kitas_registered(self):
        self.test_regwna_page()
        Select(self.verification_method()).select_by_visible_text("Online Verification (Video Call)")
        self.number_kitas_input().send_keys('12')
        kitas_taken = self.kitas_registered().text
        delay(1)

    def test_passport_registered(self):
        self.test_regwna_page()
        Select(self.verification_method()).select_by_visible_text("Online Verification (Video Call)")
        self.number_kitas_input().send_keys('098766')
        self.number_passport_input().send_keys('12')
        passport_taken = self.passport_registered().text
        delay(1)

    def test_personal_identity(self):
        self.test_regwna_page()
        Select(self.verification_method()).select_by_visible_text("Online Verification (Video Call)")
        self.number_kitas_input().send_keys('098766')
        self.number_passport_input().send_keys('093')
        self.name_input().send_keys('Aisy')
        self.birth_input().send_keys('jepang')
        self.national_input().send_keys('Jepang')
        Select(self.select_gender()).select_by_visible_text("Female")
        Select(self.select_day()).select_by_visible_text("22")
        Select(self.select_month()).select_by_visible_text("Ags")
        Select(self.select_year()).select_by_visible_text("1997")
        self.button_next().click()
        delay(3)
    def account_information(self):
        self.test_personal_identity()
        self.email_input().send_keys('dstest8@tandatanganku.com')
        self.email_input().send_keys('0890123457')
        delay(3)


    def photo_upload(self):
        self.test_personal_identity()
        self.account_information()
        self