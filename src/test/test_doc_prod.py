import main


class TestDocProd(main.TestWebsite):
    def test_pertama(self):
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
        main.delay(1)
        self.document_object("check_doc3").click()
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

