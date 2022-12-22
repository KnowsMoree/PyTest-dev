import main
from main import TestWebsite


class TestReg(TestWebsite):
    def test_reg(self):
        TestWebsite.reg_object(self, "link_reg").click()
        main.delay(5)

    def test_reg_nik(self):
        TestWebsite.reg_object(self, "link_reg").click()
        TestWebsite.reg_object(self, "uname").send_keys("8928839489849203")
        main.delay(3)

