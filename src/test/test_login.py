import main


class TestLogin(main.FormObject):
    def test_login(self):
        self.username().send_keys("ditest10@tandatanganku.com" + self.keys.ENTER)
        main.delay(2)
        self.password().send_keys("Coba1234" + self.keys.ENTER)
        main.delay(3)
        assert self.saldo_sign() is not None

    def test_password_false(self):
        self.username().send_keys("ditest10@tandatanganku.com" + self.keys.ENTER)
        main.delay(2)
        self.password().send_keys("kijang" + self.keys.ENTER)
        main.delay(5)
        assert self.password_salah() is not None

    def test_username_false(self):
        self.username().send_keys("cuicui" + self.keys.ENTER)
        main.delay(5)
        assert self.error_username() is not None

    def test_block_username(self):
        for i in range(4):
            self.username().send_keys("cuicui" + self.keys.ENTER)
            self.username().clear()
            if i is 3:
                main.delay(3)
            else:
                main.delay(1)

        assert self.error_username() is not None

    def test_block_password(self):
        for i in range(4):
            self.username().send_keys("ditest10@tandatanganku.com" + self.keys.ENTER)
            main.delay(1)
            self.password().send_keys("testing6" + self.keys.ENTER)
            main.delay(2)

        assert self.pass_error() is not None
