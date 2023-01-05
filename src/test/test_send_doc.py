import main


class TestSendDocument(main.FormObject, main.DocObject):
    def test_send_document_full(self):
        self.username().send_keys("wahyuhidy" + self.keys.ENTER)
        main.delay(2)
        self.password().send_keys("Kijang321!" + self.keys.ENTER)
        main.delay(4)
        self.choose_account().click()

        main.delay(4)

        self.doc_file().send_keys("C:\\Users\\dignitas\\Downloads\\company_image_20221101065745 (1) (1).pdf")
        main.delay(2)
        self.doc_submit().click()

        main.delay(2)

        self.check_seal_doc().click()
        self.name_first_receiver().send_keys("digisign")
        self.email_first_receiver().send_keys("ditest10@tandatanganku.com")
        self.btn_detail_doc().click()
        main.delay(2)
        self.btn_add_sign().click()

        main.delay(4)

        self.actions.drag_and_drop_by_offset(self.sign_zone_1(), 10, 150).perform()
        self.actions.drag_and_drop_by_offset(self.resizing_zone_1(), 30, 20).perform()

        main.delay(5)

        self.lock_sign_1().click()
        self.btn_set_email().click()
        self.btn_send_doc().click()
        self.process_send_doc().click()

        main.delay(10)

    def test_send_document(self):
        self.username().send_keys("ditest10@tandatanganku.com" + self.keys.ENTER)
        main.delay(2)
        self.password().send_keys("Coba1234" + self.keys.ENTER)
        main.delay(3)
        self.doc_file().send_keys("C:\\Users\\dignitas\\Downloads\\company_image_20221101065745 (1) (1).pdf")
        main.delay(4)
        self.doc_submit().click()

        main.delay(2)
