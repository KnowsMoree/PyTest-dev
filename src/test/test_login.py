import time

from main import delay, FormObject


class TestLogin(FormObject):
    def test_login(self):
        self.username().send_keys("ditest6@tandatanganku.com" + self.keys.ENTER)
        delay(2)
        first = time.time()
        self.password().send_keys("Coba1234" + self.keys.ENTER)
        last = time.time() - first
        delay(3)
        assert self.saldo_sign() is not None
        print(f"\ntime to login {time.strftime('%H:%M:%S', time.gmtime(last))}")

    def test_password_false(self):
        self.username().send_keys("ditest6@tandatanganku.com" + self.keys.ENTER)
        delay(2)
        self.password().send_keys("kijang" + self.keys.ENTER)
        delay(5)
        assert self.password_salah() is not None

    def test_username_false(self):
        self.username().send_keys("cuicui" + self.keys.ENTER)
        delay(5)
        assert self.error_username() is not None

    def test_block_username(self):
        for i in range(4):
            self.username().send_keys("cuicui" + self.keys.ENTER)
            self.username().clear()
            if i is 3:
                delay(3)
            else:
                delay(1)

        assert self.error_username() is not None

    def test_block_password(self):
        for i in range(4):
            self.username().send_keys("ditest6@tandatanganku.com" + self.keys.ENTER)
            delay(1)
            self.password().send_keys("testing6" + self.keys.ENTER)
            delay(2)

        assert self.pass_error() is not None
