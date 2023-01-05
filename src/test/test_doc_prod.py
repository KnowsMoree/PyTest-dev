import main
from selenium.webdriver.support.ui import Select


class TestDocProd(main.DocObject, main.FormObject):
    def test_upload_doc_on_email_corp(self):
        self.username().send_keys("wahyuhidy" + self.keys.ENTER)
        main.delay(2)
        self.password().send_keys("Kijang321!" + self.keys.ENTER)

        main.delay(1)

        self.choose_account().click()

        main.delay(2)

        self.doc_file().send_keys("C:\\Users\\dignitas\\Downloads\\company_image_20221101065745 (1) (1).pdf")
        self.doc_submit().click()

        main.delay(2)

        self.check_seal_doc().click()
        self.name_first_receiver().send_keys("digisign")
        self.email_first_receiver().send_keys("ditest10@tandatanganku.com")
        self.btn_detail_doc().click()
        self.btn_add_sign().click()

        main.delay(4)

        self.actions.drag_and_drop_by_offset(self.sign_zone_1(), 10, 150).perform()
        self.actions.drag_and_drop_by_offset(self.resizing_zone_1(), 30, 20).perform()

        main.delay(5)

        self.lock_sign_1().click()
        self.btn_set_email().click()
        self.btn_send_doc().click()
        self.process_send_doc().click()

        main.delay(10)

    def test_need_sign(self):
        self.username().send_keys("ditest10@tandatanganku.com" + self.keys.ENTER)
        self.password().send_keys("Coba1234" + self.keys.ENTER)
        main.delay(2)
        self.need_sign().click()
        main.delay(1)
        self.check_doc1().click()
        self.check_doc2().click()
        self.sign_all_btn().click()
        self.proses_btn().click()
        self.otp_email().click()
        main.delay(25)
        self.proses_doc_btn_submit().click()
        main.delay(3)
        self.yakin_btn().click()
        main.delay(3)
        self.btn_selesai().click()
        main.delay(5)

    def test_kotak_masuk(self):
        self.username().send_keys("ditest10@tandatanganku.com" + self.keys.ENTER)
        self.password().send_keys("Coba1234" + self.keys.ENTER)
        main.delay(2)
        self.nav_inbox().click()
        self.kotak_masuk().click()
        Select(self.filter_action()).select_by_visible_text("Need Action")
        main.delay(1)
        self.check_doc3().click()
        self.check_doc4().click()
        self.sign_all_btn().click()
        self.proses_btn().click()
        self.otp_email().click()
        main.delay(25)
        self.proses_doc_btn_submit().click()
        main.delay(3)
        self.yakin_btn().click()
        main.delay(3)
        self.btn_selesai().click()
        main.delay(5)

    def test_only_direct_doc(self):
        self.username().send_keys("ditest10@tandatanganku.com" + self.keys.ENTER)
        self.password().send_keys("Coba1234", self.keys.ENTER)
        main.delay(2)
        self.link_tooltip1().click()
        main.delay(4)

    def test_continue_direct_doc(self):
        self.test_only_direct_doc()
        self.button_proses_sign_one().click()
        main.delay(2)
        assert self.modal_title_process() is not None

    def test_agreement_process(self):
        self.test_continue_direct_doc()
        self.label_iya().click()
        main.delay(3)

    def test_denial_process(self):
        self.test_continue_direct_doc()
        self.label_tidak().click()

        main.delay(3)
        assert self.text_area_reason() is not None

    def test_otp_sms_process(self):
        self.test_continue_direct_doc()
        self.btn_otp_sms().click()
        main.delay(3)

    def test_otp_email_process(self):
        self.test_continue_direct_doc()
        self.btn_otp_email().click()
        main.delay(3)

    def test_otp_false(self):
        self.test_otp_email_process()
        self.otp_input_number().send_keys("002383")
        main.delay(3)

        self.btn_prosign().click()
        self.btn_saya_yakin().click()
        main.delay(3)

        assert self.title_verify_false() is not None
        self.btn_swal_ok().click()
        main.delay(2)

    def test_not_sure_process(self):
        self.test_continue_direct_doc()
        self.btn_prosign().click()
        self.btn_tidak_yakin().click()
        main.delay(2)

        assert self.title_proses_dibatalkan() is not None

        self.btn_swal_ok().click()
        main.delay(2)

        assert self.title_modal_proses() is not None

    def test_sure_process(self):
        self.test_otp_email_process()

        check = self.btn_gagal_otp().is_displayed()

        print(f"\nbutton gagal is {check}")

        if check is True:
            self.btn_gagal_otp().click()
            main.delay(3)
        elif check is False:
            main.delay(1)
            self.btn_prosign().click()
            main.delay(2)
            self.btn_saya_yakin().click()
            main.delay(2)
        else:
            pass
