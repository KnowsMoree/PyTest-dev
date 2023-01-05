import main


class DocObject(main.TestWebsite):
    def filter_action(self):
        return self.driver.find_element(self.by.XPATH, "//select[@name='status']")

    def filter_submit(self):
        return self.driver.find_element(self.by.XPATH, "//button[contains(@type, 'submit')]")

    def choose_account(self):
        return self.driver.find_element(self.by.XPATH, "/html/body/div/div/div/div/section/form/a[1]/div")

    def check_seal_doc(self):
        return self.driver.find_element(self.by.XPATH, "//label[.//*[@id='ckseal']]")

    def nav_inbox(self):
        return self.driver.find_element(self.by.XPATH, "//li[.//i[@class='ti-write']]")

    def kotak_masuk(self):
        return self.driver.find_element(
            self.by.XPATH, "/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/nav/ul/li[2]/ul/li[3]/a")

    def name_first_receiver(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='name-1']")

    def btn_detail_doc(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='detail_doc']")

    def btn_add_sign(self):
        return self.driver.find_element(self.by.XPATH, "//button[@onclick='adds_ttd()']")

    def sign_zone_1(self):
        return self.driver.find_element(self.by.XPATH, "//div[@class='foo blue ui-resizable']")

    def lock_sign_1(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='lock1']")

    def resizing_zone_1(self):
        return self.driver.find_element(self.by.XPATH, "//div[contains(@class, 'ui-icon')]")

    def btn_set_email(self):
        return self.driver.find_element(
            self.by.XPATH, "/html/body/div[1]/div[2]/div[2]/div[16]/div/div/div/div/div/div[3]/button")

    def process_send_doc(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='pros']")

    def btn_send_doc(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='send']")

    def need_sign(self):
        return self.driver.find_element(self.by.XPATH, "//a[contains(@href, 'needsign')]")

    def check_all_sign(self):
        return self.driver.find_element(self.by.XPATH, "//label[@for='idbox']")

    def sign_all_btn(self):
        return self.driver.find_element(self.by.XPATH, "//button[@id='signnow']")

    def email_first_receiver(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='email-1']")

    def proses_btn(self):
        return self.driver.find_element(self.by.XPATH, "//button[contains(@class, 'swal2-confirm')]")

    def check_doc1(self):
        return self.driver.find_element(self.by.XPATH, "//label[@for='checkbox1']")

    def check_doc2(self):
        return self.driver.find_element(self.by.XPATH, "//label[@for='checkbox2']")

    def check_doc3(self):
        return self.driver.find_element(self.by.XPATH, "//label[@for='checkbox3']")

    def check_doc4(self):
        return self.driver.find_element(self.by.XPATH, "//label[@for='checkbox4']")

    def otp_input_number(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='otp']")

    def otp_email(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='otemail']")

    def proses_doc_btn_submit(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='ps12']")

    def yakin_btn(self):
        return self.driver.find_element(self.by.XPATH, "//button[contains(@class, 'swal2-confirm')]")

    def link_tooltip1(self):
        return self.driver.find_element(
            self.by.XPATH,
            "/html/body/div[1]/div[2]/div[2]/div[11]/div[6]/div/div/div[1]/div/div/div/div[2]/div[3]/div/span/a")

    def btn_selesai(self):
        return self.driver.find_element(self.by.XPATH, "//a[@class='btn btn-info']")

    def button_proses_sign_one(self):
        return self.driver.find_element(self.by.XPATH, "//button[@onclick='proOtp()']")

    def modal_title_process(self):
        return self.driver.find_element(self.by.XPATH, "/html/body/div[15]/div/div/div[1]/h4")

    def label_iya(self):
        return self.driver.find_element(self.by.XPATH, "//label[@for='p1']")

    def label_tidak(self):
        return self.driver.find_element(self.by.XPATH, "//label[@for='p2']")

    def text_area_reason(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='reason']")

    def btn_otp_sms(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='btnotp']")

    def btn_otp_email(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='otemail']")

    def btn_prosign(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='prosign']")

    def title_verify_false(self):
        return self.driver.find_element(self.by.XPATH, "//*[text() = 'Kode verifikasi salah']")

    def btn_saya_yakin(self):
        return self.driver.find_element(self.by.XPATH, "//button[contains(@class, 'swal-button--confirm')]")

    def verify_false(self):
        return self.driver.find_element(self.by.XPATH, "//*[text() = 'Kode verifikasi salah']")

    def btn_swal_ok(self):
        return self.driver.find_element(self.by.XPATH, "//button[contains(@class, 'swal-button')]")

    def btn_tidak_yakin(self):
        return self.driver.find_element(self.by.XPATH, "//button[contains(@class, 'swal-button--cancel')]")

    def title_proses_dibatalkan(self):
        return self.driver.find_element(self.by.XPATH, "//*[text() = 'Proses dibatalkan']")

    def title_modal_proses(self):
        return self.driver.find_element(self.by.XPATH, "/html/body/div[15]/div/div/div[1]/h4")

    def btn_gagal_otp(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='bModal']")
