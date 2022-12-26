import main


class TestLogin(main.TestWebsite):
    def test_login(self):
        self.is_open = False
        self.is_quit = False
        self.reg_and_log_object("uname").send_keys("ditest10@tandatanganku.com" + self.keys.ENTER)
        self.reg_and_log_object("password").send_keys("Coba1234" + self.keys.ENTER)
        main.delay(3)
        assert self.reg_and_log_object("saldo_sign") is not None

    def test_password_false(self):
        self.is_open = False
        self.is_quit = False
        self.reg_and_log_object("uname").send_keys("ditest10@tandatanganku.com" + self.keys.ENTER)
        self.reg_and_log_object("password").send_keys("kijang" + self.keys.ENTER)
        main.delay(5)
        assert self.reg_and_log_object("password_salah") is not None

    def test_username_false(self):
        self.is_open = False
        self.is_quit = False
        self.reg_and_log_object("uname").send_keys("cuicui" + self.keys.ENTER)
        main.delay(5)
        assert self.reg_and_log_object("error_username") is not None

    def test_block_username(self):
        self.is_open = False
        self.is_quit = False
        for i in range(4):
            self.reg_and_log_object("uname").send_keys("cuicui" + self.keys.ENTER)
            self.reg_and_log_object("uname").clear()
            if i is 3:
                main.delay(3)
            else:
                main.delay(1)

        assert self.reg_and_log_object("error_username") is not None

    def test_block_password(self):
        self.is_open = True
        self.is_quit = True
        for i in range(4):
            self.reg_and_log_object("uname").send_keys("ditest10@tandatanganku.com" + self.keys.ENTER)
            self.reg_and_log_object("password").send_keys("testing6" + self.keys.ENTER)
            main.delay(2)

        assert self.reg_and_log_object("pass_error") is not None
