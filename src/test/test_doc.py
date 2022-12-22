import main
from main import TestWebsite


class TestDoc(main.TestWebsite):
    def test_upload_doc(self):
        TestWebsite.reg_object(self, "uname").send_keys("ditest6@tandatanganku.com" + self.keys.ENTER)
        TestWebsite.reg_object(self, "password").send_keys("Coba1234" + self.keys.ENTER)
        main.delay(2)
        TestWebsite.reg_object(self, "doc_file").send_keys(
            "C:\\Users\\dignitas\\Downloads\\company_image_20221101065745 (1) (1).pdf")
        TestWebsite.reg_object(self, "doc_submit").click()
        main.delay(4)
