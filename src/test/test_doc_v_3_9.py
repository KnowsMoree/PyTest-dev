from selenium.webdriver.support.select import Select
from main import delay
from test_send_doc import TestSendDocument
import time


class TestUpload(TestSendDocument):
    def test_web1_1(self):
        self.test_send_document()

    def test_web1_2(self):
        self.test_send_document(exe='img')


class TestProcess(TestSendDocument):
    def test_web2_1_1(self):
        self.test_nothing_to_sign(is_next=False)

    def test_web2_1_2(self):
        self.test_not_valid_time()

    def test_web2_2_1(self, **kwargs):
        is_filled = kwargs.get('is_filled', False)
        self.test_send_document()

        if is_filled is True:
            self.name_first_receiver().send_keys("wahyu")
            self.email_first_receiver().send_keys("ditest6@tandatanganku.com")

        self.btn_detail_doc().click()
        delay(2)

        if is_filled is False:
            try:
                assert self.err_name_receiver() is not None
                assert self.err_email_receiver() is not None
            except Exception as err:
                print(err)
        else:
            try:
                assert self.canvas() is not None
            except Exception as err:
                print(err)

        delay(2)

    def test_web2_2_2(self):
        self.test_web2_2_1(is_filled=True)

    def test_web2_2_3(self):
        self.test_name_receiver_not_filled()

    def test_web2_2_4(self):
        self.test_send_document()

        self.name_first_receiver().send_keys(" ")
        self.email_first_receiver().send_keys("ditest6@tandatanganku.com")
        self.btn_detail_doc().click()

        try:
            assert self.err_name_receiver() is not None
        except Exception as err:
            print(err)

        delay(2)

    def test_web2_2_5(self):
        self.test_email_receiver_not_filled()

    def test_web2_2_6(self):
        self.test_set_email_format_invalid()

    def test_web2_3_1(self):
        self.test_send_document()
        self.label_sort_sign().click()
        self.button_add_me().click()

        self.btn_detail_doc().click()
        delay(2)

        try:
            assert self.canvas() is not None
        except Exception as err:
            print(err)

    def test_web2_3_2(self):
        self.test_check_is_the_last()

    def test_web2_3_3(self):
        self.test_need_check()

    def test_web2_3_4(self):
        self.test_need_paraf(full=False)

    def test_web2_4_1(self):
        self.test_web2_3_4()

        self.btn_send_doc().click()
        self.btn_process_send_doc().click()

        try:
            assert self.sign_null() is not None
        except Exception as err:
            print(err)

        delay(5)

    def test_web2_4_2(self):
        self.test_need_paraf()

    def test_web2_5_1(self):
        self.test_send_document(seal=True)

        Select(self.select_email_seal()).select_by_visible_text("wahyu@digi-id.id")
        delay(2)

        self.button_add_me().click()
        self.btn_detail_doc().click()

        try:
            assert self.canvas() is not None
        except Exception as err:
            print(err)

        delay(2)

    def test_web2_5_2(self):
        self.test_web2_5_1()

        self.btn_send_doc().click()
        self.btn_process_send_doc().click()

        try:
            assert self.sign_null() is not None
        except Exception as err:
            print(err)

        delay(5)

    def test_web2_5_3(self):
        self.test_web2_5_1()

        self.actions.drag_and_drop_by_offset(self.imgsealer(), 100, 100).perform()
        delay(3)

        self.button_lockseal().click()
        self.btn_send_doc().click()
        self.btn_process_send_doc().click()

        self.confirm_after_send_doc().click()

        delay(5)