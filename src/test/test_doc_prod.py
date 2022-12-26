import main


class TestDocProd(main.TestWebsite):
    def test_pertama(self):
        self.reg_and_log_object("uname").send_keys("ditest10@tandatanganku.com" + self.keys.ENTER)
        self.reg_and_log_object("password").send_keys("Coba1234" + self.keys.ENTER)
        main.delay(7)
        self.document_object("need_sign").click()
