import main


class TestLogin(main.TestWebsite):
    def test_login(self):
        self.reg_object("uname").send_keys("ditest6@tandatanganku.com" + self.keys.ENTER)
        self.reg_object("password").send_keys("Coba1234" + self.keys.ENTER)
        main.delay(3)
        assert self.reg_object("saldo_sign") is not None
