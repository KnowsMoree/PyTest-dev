import main


class TestDoc(main.TestWebsite):
    def test_upload_doc(self):
        uname = self.browser.find_element(self.by.XPATH, "//*[@id='username']")
        uname.send_keys("ditest6@tandatanganku.com" + self.keys.ENTER)
        pw = self.browser.find_element(self.by.XPATH, "//input[@id='pd']")
        pw.send_keys("Coba1234" + self.keys.ENTER)
        main.delay(2)
        file = self.browser.find_element(self.by.XPATH, "//input[@type='file']")
        file.send_keys("C:\\Users\\dignitas\\Downloads\\company_image_20221101065745 (1) (1).pdf")
        self.browser.find_element(self.by.XPATH, "//button[@type='submit']").click()
        main.delay(4)
