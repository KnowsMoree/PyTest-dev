import main


class TestReg(main.TestWebsite):
    def test_reg(self):
        self.reg_object("link_reg").click()
        main.delay(5)

    def test_reg_nik(self):
        self.reg_object("link_reg").click()
        self.reg_object("uname").send_keys("8928839489849203")
        main.delay(3)
