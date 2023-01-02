import main


class TestDocProd(main.TestWebsite):
    def test_upload_doc_on_email_corp(self):
        self.driver.maximize_window()
        self.reg_and_log_object("uname").send_keys("wahyuhidy" + self.keys.ENTER)
        self.reg_and_log_object("password").send_keys("Kijang321!" + self.keys.ENTER)

        main.delay(1)

        self.document_object("choose_account").click()

        main.delay(2)

        self.reg_and_log_object("doc_file").send_keys(
            "C:\\Users\\dignitas\\Downloads\\company_image_20221101065745 (1) (1).pdf")
        self.reg_and_log_object("doc_submit").click()

        main.delay(2)

        self.document_object("check_seal_doc").click()
        self.document_object("name_first_receiver").send_keys("digisign")
        self.document_object("email_first_receiver").send_keys("ditest10@tandatanganku.com")
        self.document_object("btn_detail_doc").click()
        self.document_object("btn_add_sign").click()

        main.delay(4)

        self.actions.drag_and_drop_by_offset(self.document_object("sign_zone_1"), 10, 150).perform()
        self.actions.drag_and_drop_by_offset(self.document_object("resizing_zone_1"), 30, 20).perform()

        main.delay(5)

        self.document_object("lock_sign_1").click()
        self.document_object("btn_set_email").click()
        self.document_object("btn_send_doc").click()
        self.document_object("process_send_doc").click()

        main.delay(10)

    def test_need_sign(self):
        self.reg_and_log_object("uname").send_keys("ditest10@tandatanganku.com" + self.keys.ENTER)
        self.reg_and_log_object("password").send_keys("Coba1234" + self.keys.ENTER)
        main.delay(2)
        self.document_object("need_sign").click()
        main.delay(1)
        self.document_object("check_doc1").click()
        self.document_object("check_doc2").click()
        self.document_object("sign_all_btn").click()
        self.document_object("proses_btn").click()
        self.document_object("otp_email").click()
        main.delay(25)
        self.document_object("proses_doc_btn_submit").click()
        main.delay(3)
        self.document_object("yakin_btn").click()
        main.delay(3)
        self.document_object("btn_selesai").click()
        main.delay(5)

    def test_kotak_masuk(self):
        self.reg_and_log_object("uname").send_keys("ditest10@tandatanganku.com" + self.keys.ENTER)
        self.reg_and_log_object("password").send_keys("Coba1234" + self.keys.ENTER)
        main.delay(2)
        self.document_object("nav_inbox").click()
        self.document_object("kotak_masuk").click()
        main.select_option(self.document_object("filter_action")).select_by_visible_text("Need Action")
        main.delay(1)
        self.document_object("check_doc3").click()
        self.document_object("check_doc4").click()
        self.document_object("sign_all_btn").click()
        self.document_object("proses_btn").click()
        self.document_object("otp_email").click()
        main.delay(25)
        self.document_object("proses_doc_btn_submit").click()
        main.delay(3)
        self.document_object("yakin_btn").click()
        main.delay(3)
        self.document_object("btn_selesai").click()
        main.delay(5)

    def test_only_direct_doc(self):
        self.reg_and_log_object("uname").send_keys("ditest10@tandatanganku.com" + self.keys.ENTER)
        self.reg_and_log_object("password").send_keys("Coba1234", self.keys.ENTER)
        main.delay(2)
        self.document_object("link_tooltip1").click()
        main.delay(4)

    def test_continue_direct_doc(self):
        self.test_only_direct_doc()
        self.document_object("button_proses_sign_one").click()
        main.delay(2)
        assert self.document_object("modal_title_process") is not None

    def test_agreement_process(self):
        self.test_continue_direct_doc()
        self.document_object("label_iya").click()
        main.delay(3)

    def test_denial_process(self):
        self.test_continue_direct_doc()
        self.document_object("label_tidak").click()

        main.delay(3)
        assert self.document_object("text_area_reason") is not None

    def test_otp_sms_process(self):
        self.test_continue_direct_doc()
        self.document_object("btn_otp_sms").click()
        main.delay(3)

    def test_otp_email_process(self):
        self.test_continue_direct_doc()
        self.document_object("btn_otp_email").click()
        main.delay(3)

    def test_otp_false(self):
        self.test_continue_direct_doc()
        self.document_object("btn_otp_email").click()
        main.delay(0.5)
        self.document_object("otp_input_number").send_keys("002383")
        main.delay(3)

        self.document_object("btn_prosign").click()
        self.document_object("btn_saya_yakin").click()
        main.delay(3)

        assert self.document_object("title_verify_false") is not None
        self.document_object("btn_swal_ok").click()
        main.delay(2)

    def test_not_sure_process(self):
        self.test_continue_direct_doc()
        self.document_object("btn_prosign").click()
        self.document_object("btn_tidak_yakin").click()
        main.delay(2)

        assert self.document_object("title_proses_dibatalkan") is not None

        self.document_object("btn_swal_ok").click()
        main.delay(2)

        assert self.document_object("title_modal_proses") is not None

    def test_sure_process(self):
        self.test_otp_email_process()

        check = self.document_object("btn_gagal_otp").is_displayed()

        print(f"\nbutton gagal is {check}")

        if check is True:
            self.document_object("btn_gagal_otp").click()
            main.delay(3)
        elif check is False:
            main.delay(1)
            self.document_object("btn_prosign").click()
            main.delay(2)
            self.document_object("btn_saya_yakin").click()
            main.delay(2)
        else:
            pass
