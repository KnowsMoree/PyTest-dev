from selenium.webdriver.support.select import Select

from main import delay, DocObject, FormObject


class TestSendDocument(FormObject, DocObject):
    def test_send_document(self):
        self.username().send_keys("ditest6@tandatanganku.com" + self.keys.ENTER)
        delay(2)
        self.password().send_keys("Coba1234" + self.keys.ENTER)
        delay(4)
        # self.choose_account().click()
        delay(3)
        self.doc_file().send_keys("C:\\Users\\dignitas\\Downloads\\company_image_20221101065745 (1) (1).pdf")
        delay(4)
        self.doc_submit().click()
        delay(2)

    def test_need_check(self, **kwargs):
        select = kwargs.get('select', "Dibutuhkan Tandatangan")
        self.test_send_document()

        self.button_add_me().click()
        self.label_sort_sign().click()

        if select is "Dibutuhkan Tandatangan":
            Select(self.select_action_need()).select_by_visible_text(select)
        else:
            pass

        self.button_add_receiver().click()
        self.input_name_receiver_2().send_keys("Aziz")
        self.input_email_receiver_2().send_keys("aziz@digi-id.id")

        if select is "Dibutuhkan Tandatangan":
            self.btn_detail_doc().click()
            delay(2)
            assert self.canvas() is not None
        elif select is "Dibutuhkan Pengecekan":
            Select(self.select_action_need_2()).select_by_visible_text(select)
            self.btn_detail_doc().click()
            delay(2)
            assert self.icon_x_swal() is not None
            self.button_swal_confirm_ok().click()

    def test_not_valid_time(self):
        self.test_send_document()

        self.btn_choose_expired_date().click()

        for i in range(6):
            self.btn_previous_month_date().click()
            delay(1)

        self.date().click()
        self.button_ok_date().click()

        assert self.icon_x_swal() is not None
        delay(1)

        self.button_swal_confirm_ok().click()

    def test_nothing_to_sign(self):
        self.test_send_document()

        self.button_add_me().click()
        self.btn_detail_doc().click()

        self.btn_send_doc().click()
        self.btn_process_send_doc().click()

        assert self.icon_x_swal() is not None
        self.button_swal_confirm_ok().click()

    def test_check_is_the_last(self):
        self.test_need_check(select="Dibutuhkan Pengecekan")

    def test_set_email_format_invalid(self):
        self.test_send_document()

        self.name_first_receiver().send_keys("wayy")
        self.email_first_receiver().send_keys("ditest28")

        self.btn_detail_doc().click()
        delay(2)
        assert self.err_email_receiver() is not None

    def test_email_receiver_is_same(self):
        self.test_send_document()

        self.button_add_me().click()
        self.button_add_receiver().click()

        self.input_name_receiver_2().send_keys("wahyu")
        self.input_email_receiver_2().send_keys("ditest10@tandatanganku.com")

        self.btn_detail_doc().click()
        delay(2)
        assert self.err_email_receiver_2() is not None

    def test_email_receiver_not_filled(self):
        self.test_send_document()

        self.name_first_receiver().send_keys("wahyu")

        self.btn_detail_doc().click()
        delay(2)
        assert self.err_email_receiver() is not None

    def test_name_receiver_not_filled(self):
        self.test_send_document()

        self.email_first_receiver().send_keys("ditest10@tandatanganku.com")
        self.btn_detail_doc().click()

        assert self.err_name_receiver() is not None

    def test_need_paraf(self):
        self.test_send_document()

        self.button_add_me().click()
        Select(self.select_action_need()).select_by_visible_text("Dibutuhkan Paraf")

        self.btn_detail_doc().click()
        self.button_paraf().click()
        delay(2)

        self.actions.drag_and_drop_by_offset(self.paraf_box(), 10, 100).perform()

        self.lock_paraf_1().click()
        self.btn_set_email().click()
        self.btn_send_doc().click()
        self.btn_process_send_doc().click()

        self.confirm_after_send_doc().click()

        delay(5)

    def test_send_document_full(self, **kwargs):
        iteration = kwargs.get('iteration', 1)
        is_used = kwargs.get('is_used', False)
        size = kwargs.get('size', [30, 20])
        pos = kwargs.get('pos', [0, 0])

        if is_used is False:
            self.username().send_keys("wahyuhi" + self.keys.ENTER)
            delay(2)
            self.password().send_keys("Kijang321!" + self.keys.ENTER)
            delay(4)
            self.choose_account().click()

        for i in range(iteration):
            if is_used is False:
                delay(2)
                self.doc_file().send_keys("C:\\Users\\dignitas\\Downloads\\company_image_20221101065745 (1) (1).pdf")
                delay(2)
                self.doc_submit().click()
                delay(2)
                self.name_first_receiver().send_keys("digisign")
                self.email_first_receiver().send_keys("ditest6@tandatanganku.com")

            self.btn_detail_doc().click()
            delay(2)
            self.btn_add_sign().click()

            delay(4)

            self.actions.drag_and_drop_by_offset(self.sign_zone_1(), pos[0], pos[1]).perform()
            self.actions.drag_and_drop_by_offset(self.resizing_zone_1(), size[0], size[1]).perform()

            delay(5)

            self.lock_sign_1().click()
            delay(1)
            self.btn_set_email().click()
            self.btn_send_doc().click()
            self.btn_process_send_doc().click()
            delay(3)
            self.confirm_after_send_doc().click()
            delay(2)

            if i is len(range(iteration)) - 1:
                pass
            else:
                delay(1)
                self.link_home().click()

    def test_send_doc_with_iterator(self):
        self.test_send_document_full(iteration=3)

    def test_send_doc_on_draft(self, **kwargs):
        is_next = kwargs.get('is_next', True)
        self.username().send_keys("ditest6@tandatanganku.com" + self.keys.ENTER)
        delay(2)
        self.password().send_keys("Coba1234" + self.keys.ENTER)
        delay(2)

        self.dropdown_dokumen().click()
        self.link_draf().click()

        if is_next is True:
            self.btn_send_row_one_file_draf().click()
            self.test_send_document_full(is_used=True)

    def test_open_document_on_draft(self):
        self.test_send_doc_on_draft(is_next=False)

        self.btn_lihat_file_draf().click()
        delay(2)

        assert self.canvas() is not None

    def test_delete_document_on_draft(self):
        self.test_send_doc_on_draft(is_next=False)

        self.btn_hapus_file_draf().click()
        self.proses_btn().click()

        delay(2)


class TestSendDocumentV38(TestSendDocument):
    def test_send_document_new(self):
        self.test_send_document()

    def test_send_document_min_size_sign(self):
        self.test_send_document_full(size=[-100, -65], pos=[80, 90])
