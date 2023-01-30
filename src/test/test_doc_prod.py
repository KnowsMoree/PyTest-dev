from selenium.webdriver.support.ui import Select
from main import delay
from test_send_doc import TestSendDocument
import time


class TestDocProd(TestSendDocument):
    def test_need_sign(self):
        self.username().send_keys("ditest6@tandatanganku.com" + self.keys.ENTER)
        self.password().send_keys("Coba1234" + self.keys.ENTER)
        delay(2)
        self.need_sign().click()
        delay(1)
        self.check_doc1().click()
        self.check_doc2().click()
        self.sign_all_btn().click()
        self.proses_btn().click()
        self.otp_email().click()
        delay(25)
        self.proses_doc_btn_submit().click()
        delay(3)
        self.yakin_btn().click()
        delay(3)
        self.btn_selesai().click()
        delay(5)

    def test_kotak_masuk(self):
        self.username().send_keys("ditest6@tandatanganku.com" + self.keys.ENTER)
        self.password().send_keys("Coba1234" + self.keys.ENTER)
        delay(2)
        self.nav_inbox().click()
        self.kotak_masuk().click()
        Select(self.filter_action()).select_by_visible_text("Need Action")
        delay(1)
        self.check_doc3().click()
        self.check_doc4().click()
        self.sign_all_btn().click()
        self.proses_btn().click()
        self.otp_email().click()
        delay(25)
        self.proses_doc_btn_submit().click()
        delay(3)
        self.yakin_btn().click()
        delay(3)
        self.btn_selesai().click()
        delay(5)

    def test_direct_doc(self):
        self.username().send_keys("ditest6@tandatanganku.com" + self.keys.ENTER)
        self.password().send_keys("Coba1234", self.keys.ENTER)
        delay(2)
        self.need_sign().click()
        first = time.time()
        self.latest_inbox().click()
        last = time.time() - first
        delay(4)
        print(f"\ntime to open doc {time.strftime('%H:%M:%S', time.gmtime(last))}")

    def test_continue_direct_doc(self):
        self.test_direct_doc()
        self.button_proses_sign_one().click()
        delay(2)
        assert self.modal_title_process() is not None

    def test_agreement_process(self):
        self.test_continue_direct_doc()
        self.label_iya().click()
        delay(3)

    def test_denial_process(self):
        self.test_continue_direct_doc()
        self.label_tidak().click()

        delay(3)
        assert self.text_area_reason() is not None

    def test_otp_sms_process(self):
        self.test_continue_direct_doc()
        self.btn_otp_sms().click()
        delay(3)

    def test_otp_email_process(self, **kwargs):
        is_no_req = kwargs.get("is_no_req", False)
        self.test_continue_direct_doc()
        if is_no_req is False:
            self.btn_otp_email().click()
        else:
            delay(3)

    def test_otp_false(self, **kwargs):
        otp = kwargs.get('otp_code', "002383")
        otpless = kwargs.get('otpless', False)
        self.test_otp_email_process(is_no_req=otpless)
        self.otp_input_number().send_keys(otp)
        delay(3)

        self.btn_prosign().click()
        self.btn_saya_yakin().click()
        delay(3)

        assert self.swal_otp_none() is not None
        self.btn_swal_ok().click()
        delay(2)

    def test_not_sure_process(self):
        self.test_continue_direct_doc()
        self.btn_prosign().click()
        self.btn_tidak_yakin().click()
        delay(2)

        assert self.title_proses_dibatalkan() is not None

        self.btn_swal_ok().click()
        delay(2)

        assert self.title_modal_proses() is not None

    def test_sure_process(self):
        self.test_otp_email_process()

        check = self.btn_gagal_otp().is_displayed()

        print(f"\nbutton gagal is {check}")

        if check is True:
            self.btn_gagal_otp().click()
            delay(3)
        elif check is False:
            delay(1)
            self.btn_prosign().click()
            delay(2)
            self.btn_saya_yakin().click()
            delay(2)
        else:
            pass
