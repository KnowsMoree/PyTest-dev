import main


class TestDoc(main.TestWebsite):
    def test_upload_doc(self):
        self.driver.maximize_window()
        self.reg_and_log_object("uname").send_keys("ditest6@tandatanganku.com" + self.keys.ENTER)
        self.reg_and_log_object("password").send_keys("Coba1234" + self.keys.ENTER)
        main.delay(2)
        self.reg_and_log_object("doc_file").send_keys(
            "C:\\Users\\dignitas\\Downloads\\company_image_20221101065745 (1) (1).pdf")
        self.reg_and_log_object("doc_submit").click()
        main.delay(4)

