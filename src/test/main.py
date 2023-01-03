import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


def delay(sec):
    time.sleep(sec)


def select_option(element):
    Select(element)


class TestWebsite:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    testing_url = {
        "prod": "https://app.digisign.id/",
        "test": "https://app.tandatanganku.com"
    }

    @pytest.fixture(autouse=True)
    def browser_setup_and_teardown(self):
        self.keys = Keys
        self.by = By

        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.delete_all_cookies()

        self.driver.get(self.testing_url["prod"])

        self.actions = ActionChains(self.driver)

        yield

    def reg_and_log_object(self, element):
        """Registration Object"""
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
            case "btn_input_file":
                return self.driver.find_element(By.XPATH, "//span[@class='btn btn-danger ']")
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
            case "error_format16_nik":
                return self.driver.find_element(
                    By.XPATH, "//div[@id = 'e_idcard' and (text() = 'Harus 16 Digit.' or . = 'Harus 16 Digit.')]")
            case "error_format_false":
                return self.driver.find_element(By.XPATH, "//*[text() = 'Format NIK Salah']")
            case "birth_place_input":
                return self.driver.find_element(By.XPATH, "//*[@id='lbrith']")
            case "btn_next_step1":
                return self.driver.find_element(By.XPATH, "//button[@onclick='step1()']")
            case "validation_name":
                return self.driver.find_element(
                    By.XPATH, "//input[@id='name'][contains(@class,'form-control input-md is-invalid')]")
            case "name_input":
                return self.driver.find_element(By.XPATH, "//*[@id='name']")
            case "gender_select":
                return self.driver.find_element(By.XPATH, "//*[@id='jk']")
            case "validation_place":
                return self.driver.find_element(
                    By.XPATH, "//input[@id='lbrith'][@class='form-control input-md is-invalid']")
            case "step2":
                return self.driver.find_element(By.XPATH, "//*[text() = 'Informasi Akun']")
            case "password_reg":
                return self.driver.find_element(By.XPATH, "//*[@id='password']")
            case "password_confirmation":
                return self.driver.find_element(By.XPATH, "//*[@id='password2']")
            case "email_input_register":
                return self.driver.find_element(By.XPATH, "//*[@id='email']")
            case "phone_input_register":
                return self.driver.find_element(By.XPATH, "//*[@id='handphone']")
            case "step3":
                return self.driver.find_element(By.XPATH, "//button[@onclick='step3()']")
            case "validation_username":
                return self.driver.find_element(
                    By.XPATH, "//input[@id='username'][@class='form-control input-md is-invalid']")
            case "err_username":
                return self.driver.find_element(By.XPATH, "//*[@id='e_username']")
            case "username_registered":
                return self.driver.find_element(By.XPATH, "/html/body/div[11]/form/div/div[4]/div[1]/div/div[2]/i")
            case "password_too_short":
                return self.driver.find_element(By.XPATH, "//*[text() = 'Password terlalu pendek, min 8 character']")
            case "password_minus_symbol":
                return self.driver.find_element(
                    By.XPATH, "//*[text() = 'Password harus mengandung minimal 1 Simbol/Karakter Spesial']")
            case "strong_password":
                return self.driver.find_element(By.XPATH, "//*[text() = 'Strong password']")
            case "pass_not_same":
                return self.driver.find_element(By.XPATH, "//*[@id='e_password2']")
            case "validation_email":
                return self.driver.find_element(
                    By.XPATH, "//input[@id='email'][@class='form-control input-md is-invalid']")
            case "email_taken":
                return self.driver.find_element(By.XPATH, "//*[text() = 'Email sudah terdaftar gunakan email lain']")
            case "email_invalid":
                return self.driver.find_element(By.XPATH, "//*[text() = 'Invalid Email Address']")
            case "number_invalid":
                return self.driver.find_element(
                    By.XPATH, "//input[@id='handphone'][@class='NumOnly form-control input-md is-invalid']")
            case "false_number_format":
                return self.driver.find_element(By.XPATH, "//*[text() = 'Format nomor salah']")
            case "number_less_than_8":
                return self.driver.find_element(By.XPATH, "//*[text() = 'Nomor HP Minimal 8 digit']")

    def document_object(self, element):
        match element:
            case "filter_action":
                return self.driver.find_element(By.XPATH, "//select[@name='status']")
            case "filter_submit":
                return self.driver.find_element(By.XPATH, "//button[contains(@type, 'submit')]")
            case "choose_account":
                return self.driver.find_element(By.XPATH, "/html/body/div/div/div/div/section/form/a[1]/div")
            case "check_seal_doc":
                return self.driver.find_element(By.XPATH, "//label[.//*[@id='ckseal']]")
            case "nav_inbox":
                return self.driver.find_element(By.XPATH, "//li[.//i[@class='ti-write']]")
            case "kotak_masuk":
                return self.driver.find_element(
                    By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/nav/ul/li[2]/ul/li[3]/a")
            case "name_first_receiver":
                return self.driver.find_element(By.XPATH, "//*[@id='name-1']")
            case "link_tooltip1":
                return self.driver.find_element(
                    By.XPATH,
                    "/html/body/div[1]/div[2]/div[2]/div[11]/div[6]/div/div/div[1]/div/div/div/div[2]/div[3]/div/span/a"
                )
            case "email_first_receiver":
                return self.driver.find_element(By.XPATH, "//*[@id='email-1']")
            case "btn_detail_doc":
                return self.driver.find_element(By.XPATH, "//*[@id='detail_doc']")
            case "btn_add_sign":
                return self.driver.find_element(By.XPATH, "//button[@onclick='adds_ttd()']")
            case "sign_zone_1":
                return self.driver.find_element(By.XPATH, "//div[@class='foo blue ui-resizable']")
            case "lock_sign_1":
                return self.driver.find_element(By.XPATH, "//*[@id='lock1']")
            case "resizing_zone_1":
                return self.driver.find_element(By.XPATH, "//div[contains(@class, 'ui-icon')]")
            case "btn_set_email":
                return self.driver.find_element(
                    By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[16]/div/div/div/div/div/div[3]/button")
            case "process_send_doc":
                return self.driver.find_element(By.XPATH, "//*[@id='pros']")
            case "btn_send_doc":
                return self.driver.find_element(By.XPATH, "//*[@id='send']")
            case "need_sign":
                return self.driver.find_element(By.XPATH, "//a[contains(@href, 'needsign')]")
            case "check_all_sign":
                return self.driver.find_element(By.XPATH, "//label[@for='idbox']")
            case "sign_all_btn":
                return self.driver.find_element(By.XPATH, "//button[@id='signnow']")
            case "proses_btn":
                return self.driver.find_element(By.XPATH, "//button[contains(@class, 'swal2-confirm')]")
            case "check_doc1":
                return self.driver.find_element(By.XPATH, "//label[@for='checkbox1']")
            case "check_doc2":
                return self.driver.find_element(By.XPATH, "//label[@for='checkbox2']")
            case "check_doc3":
                return self.driver.find_element(By.XPATH, "//label[@for='checkbox3']")
            case "check_doc4":
                return self.driver.find_element(By.XPATH, "//label[@for='checkbox4']")
            case "otp_input_number":
                return self.driver.find_element(By.XPATH, "//*[@id='otp']")
            case "otp_email":
                return self.driver.find_element(By.XPATH, "//*[@id='otemail']")
            case "proses_doc_btn_submit":
                return self.driver.find_element(By.XPATH, "//*[@id='ps12']")
            case "yakin_btn":
                return self.driver.find_element(By.XPATH, "//button[contains(@class, 'swal2-confirm')]")
            case "btn_selesai":
                return self.driver.find_element(By.XPATH, "//a[@class='btn btn-info']")
            case "button_proses_sign_one":
                return self.driver.find_element(By.XPATH, "//button[@onclick='proOtp()']")
            case "modal_title_process":
                return self.driver.find_element(By.XPATH, "/html/body/div[15]/div/div/div[1]/h4")
            case "label_iya":
                return self.driver.find_element(By.XPATH, "//label[@for='p1']")
            case "label_tidak":
                return self.driver.find_element(By.XPATH, "//label[@for='p2']")
            case "text_area_reason":
                return self.driver.find_element(By.XPATH, "//*[@id='reason']")
            case "btn_otp_sms":
                return self.driver.find_element(By.XPATH, "//*[@id='btnotp']")
            case "btn_otp_email":
                return self.driver.find_element(By.XPATH, "//*[@id='otemail']")
            case "btn_prosign":
                return self.driver.find_element(By.XPATH, "//*[@id='prosign']")
            case "title_verify_false":
                return self.driver.find_element(By.XPATH, "//*[text() = 'Kode verifikasi salah']")
            case "btn_saya_yakin":
                return self.driver.find_element(By.XPATH, "//button[contains(@class, 'swal-button--confirm')]")
            case "verify_false":
                return self.driver.find_element(By.XPATH, "//*[text() = 'Kode verifikasi salah']")
            case "btn_swal_ok":
                return self.driver.find_element(By.XPATH, "//button[contains(@class, 'swal-button')]")
            case "btn_tidak_yakin":
                return self.driver.find_element(By.XPATH, "//button[contains(@class, 'swal-button--cancel')]")
            case "title_proses_dibatalkan":
                return self.driver.find_element(By.XPATH, "//*[text() = 'Proses dibatalkan']")
            case "title_modal_proses":
                return self.driver.find_element(By.XPATH, "/html/body/div[15]/div/div/div[1]/h4")
            case "btn_gagal_otp":
                return self.driver.find_element(By.XPATH, "//*[@id='bModal']")
