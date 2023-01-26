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

    def lock_paraf_1(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='lockinit1']")

    def resizing_zone_1(self):
        return self.driver.find_element(self.by.XPATH, "//div[contains(@class, 'ui-icon')]")

    def btn_set_email(self):
        return self.driver.find_element(
            self.by.XPATH, "/html/body/div[1]/div[2]/div[2]/div[16]/div/div/div/div/div/div[3]/button")

    def btn_process_send_doc(self):
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
            "/html/body/div[1]/div[2]/div[2]/div/div[4]/div/div/div[1]/div/div/div/div[2]/div[3]/div/span")

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

    def button_add_me(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='add_me']")

    def select_action_need(self):
        return self.driver.find_element(self.by.XPATH, "//select[@id='ck1']")

    def select_action_need_2(self):
        return self.driver.find_element(self.by.XPATH, "//select[@id='ck2']")

    def button_add_receiver(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='add_re']")

    def input_name_receiver_2(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='name-2']")

    def input_email_receiver_2(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='email-2']")

    def canvas(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='pdf-canvas']")

    def label_sort_sign(self):
        return self.driver.find_element(self.by.XPATH, "//label[@for='seq1']")

    def btn_choose_expired_date(self):
        return self.driver.find_element(self.by.XPATH, "//i[@role='right-icon']")

    def btn_previous_month_date(self):
        return self.driver.find_element(self.by.XPATH, "//i[@class='gj-icon chevron-left']")

    def date(self):
        return self.driver.find_element(self.by.XPATH, "/html/body/div[2]/div/div[2]/table/tbody/tr[3]/td[4]/div")

    def button_ok_date(self):
        return self.driver.find_element(self.by.XPATH, "/html/body/div[2]/div/div[3]/button[2]")

    def icon_x_swal(self):
        return self.driver.find_element(self.by.XPATH, "//span[@class='swal2-x-mark']")

    def button_swal_confirm_ok(self):
        return self.driver.find_element(self.by.XPATH, "//button[contains(@class, 'swal2-confirm')]")

    def err_email_receiver(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='e_email-1']")

    def err_email_receiver_2(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='e_email-2']")

    def err_name_receiver(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='e_name-1']")

    def button_paraf(self):
        return self.driver.find_element(self.by.XPATH, "//button[contains(@onclick, 'adds_init()')]")

    def paraf_box(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='imginit-1']")

    def confirm_after_send_doc(self):
        return self.driver.find_element(self.by.XPATH, "//button[contains(@style, '133,')]")

    def link_home(self):
        return self.driver.find_element(self.by.XPATH, "/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/nav/ul/li[1]/a")

    def dropdown_dokumen(self):
        return self.driver.find_element(
            self.by.XPATH, "//a[contains(@href, 'javascript:void(0)')][.//i[@class='ti-write']]")

    def link_draf(self):
        return self.driver.find_element(
            self.by.XPATH, "/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/nav/ul/li[2]/ul/li[1]/a")

    def btn_send_row_one_file_draf(self):
        return self.driver.find_element(
            self.by.XPATH, "/html/body/div[1]/div[2]/div[2]/div[12]/div/div/div/div/div/div/div[2]/div[3]/btn[3]")

    def btn_hapus_file_draf(self):
        return self.driver.find_element(
            self.by.XPATH, "/html/body/div[1]/div[2]/div[2]/div[12]/div/div/div/div/div/div/div[2]/div[3]/btn[1]")

    def btn_lihat_file_draf(self):
        return self.driver.find_element(
            self.by.XPATH, "/html/body/div[1]/div[2]/div[2]/div[12]/div/div/div/div/div/div/div[2]/div[3]/btn[2]")

    def sign_null(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='swal2-content']")

    def select_email_seal(self):
        return self.driver.find_element(self.by.XPATH, "//select[@id='seal']")

    def imgsealer(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='imgsealer']")

    def button_lockseal(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='lockseal']")

    def kotak_masuk_terakhir(self):
        return self.driver.find_element(self.by.XPATH, "//div[@data-target='#demo1']")

    def tanggal_kotak_masuk(self):
        return self.driver.find_element(
            self.by.XPATH,
            "/html/body/div[1]/div[2]/div[2]/div[11]/div[6]/div/div/div[1]/div/div/div/div[2]/div[3]/div")

    def latest_tandatangan(self):
        return self.driver.find_element(
            self.by.XPATH,
            "/html/body/div[1]/div[2]/div[2]/div[11]/div[6]/div/div/div[1]/div/div/div/div[2]/div[3]/div/span"
        )
