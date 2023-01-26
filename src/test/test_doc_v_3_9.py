import re
from datetime import datetime, timedelta

from selenium.webdriver.support.select import Select
from main import delay, MailObject
from test_send_doc import TestSendDocument
from test_doc_prod import TestDocProd


class TestUpload(TestSendDocument):
    def test_web1_1(self):
        self.test_send_document()

    def test_web1_2(self):
        self.test_send_document(exe='img')


class TestProcessSendDoc(TestSendDocument, MailObject):
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

    def test_web2_6_1(self):
        self.test_send_document_full(size=[-100, -65], pos=[80, 90])

    def test_web2_6_2(self):
        self.test_send_document_full(pos=[20, 78])

    def test_web2_6_3(self):
        self.test_send_document_full(size=[472, 236], pos=[-45, 0])

    def test_web2_7(self):
        self.test_nothing_to_sign()

    def test_web2_8(self):
        self.test_nothing_to_sign(is_not_locked=True)

    def test_web2_9(self):
        self.test_send_document()

        self.button_add_me().click()

        self.btn_detail_doc().click()

        self.btn_add_sign().click()
        self.actions.drag_and_drop_by_offset(self.sign_zone_1(), 700, 200).perform()
        delay(2)

        self.lock_sign_1().click()
        self.btn_set_email().click()
        self.btn_send_doc().click()
        self.btn_process_send_doc().click()

        try:
            assert self.sign_null() is not None
        except Exception as err:
            print(err)

        delay(2)

    def test_web2_10(self):
        self.test_send_document_full()

        self.class_variable_date = datetime.now()
        print("\n", self.class_variable_date)

    def test_web2_11(self):
        self.test_send_document_full()
        self.date_after_test = datetime.now()

        self.driver.execute_script("window.open('about:blank','tab2')")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://mail.tandatanganku.com")

        self.input_username().send_keys("ditest6@tandatanganku.com")
        self.input_password().send_keys("ditest123" + self.keys.ENTER)
        delay(5)

        for i in range(10):
            self.refresh().click()
            delay(1.5)

        self.actions.double_click(self.msg_list_1()).perform()

        date_received = self.date_get().text
        cvrt_date_received = datetime.strptime(date_received, "%B %d, %Y %I:%M %p")

        try:
            if cvrt_date_received <= self.date_after_test:
                print("\nTime send documents is below than email received")
            else:
                raise Exception("\nThe message date is not more than now")
        except Exception as e:
            print(e)

        delay(2)

    def test_web2_12(self):
        self.username().send_keys("ditest6@tandatanganku.com" + self.keys.ENTER)
        delay(2)
        self.password().send_keys("Coba1234" + self.keys.ENTER)
        delay(4)

        self.kotak_masuk_terakhir().click()
        tanggal_masuk = self.tanggal_kotak_masuk().text.split("\n")[1]

        print(tanggal_masuk, "tanggal_masuk")

        if bool(re.search('[a-zA-Z]', tanggal_masuk)) is True:
            date_time_obj = datetime.strptime(tanggal_masuk, "%d %b")
            yesterday = datetime.now() - timedelta(days=1)

            if datetime.now() >= date_time_obj > yesterday:
                delay(2)
            else:
                raise Exception("This not newest doc")
        else:
            date_time_obj = datetime.strptime(tanggal_masuk, "%H:%M").time()

            if datetime.now().time() >= date_time_obj:
                delay(2)
            else:
                raise Exception("This not newest doc")

        self.latest_tandatangan().click()

        try:
            assert self.canvas() is not None
        except Exception as e:
            print(e)


class TestProcessSignDoc(TestDocProd):
    def test_web3_1(self):
        self.test_direct_doc()

    def test_web3_2(self):
        self.username().send_keys("ditest6@tandatanganku.com" + self.keys.ENTER)
        self.password().send_keys("Coba1234", self.keys.ENTER)
        delay(2)

        self.dropdown_dokumen().click()
        self.link_terkirim().click()

        self.btn_eye().click()
        delay(2)

        try:
            assert self.canvas() is not None
        except Exception as e:
            raise e

    def test_web3_3(self):
        self.test_denial_process()

    def test_web3_4(self):
        self.test_otp_false(otp_code="", otpless=True)

    def test_web3_5(self):
        self.test_otp_false()

    def test_web3_6(self):
        """semi-automation because its receive and send otp Email"""
        self.username().send_keys("ditest6@tandatanganku.com" + self.keys.ENTER)
        self.password().send_keys("Coba1234" + self.keys.ENTER)
        self.need_sign().click()
        self.latest_inbox().click()

        self.button_proses_sign_one().click()
        self.btn_otp_email().click()

        delay(25)

        self.btn_prosign().click()
        self.btn_saya_yakin().click()
        delay(7)

    def test_web3_7(self):
        """semi-automation because its receive and send otp SMS"""
        self.username().send_keys("wahyuhi" + self.keys.ENTER)
        self.password().send_keys("Kijang321!" + self.keys.ENTER)
        self.choose_account().click()
        self.need_sign().click()

        self.latest_inbox().click()

        self.button_proses_sign_one().click()
        self.btn_otp_sms().click()

        delay(25)

        self.btn_prosign().click()
        self.btn_saya_yakin().click()
        delay(7)

    def test_web3_8(self):
        """semi-automation because its receive and send otp"""
        self.test_denial_process()

        self.text_area_reason().send_keys("testing")
        self.btn_otp_email().click()

        delay(25)

        self.btn_prosign().click()
        self.btn_saya_yakin().click()
        delay(7)

    def test_web3_9(self):
        self.test_agreement_process()

        self.btn_otp_email().click()

        delay(25)

        self.btn_prosign().click()
        self.btn_saya_yakin().click()
        delay(7)

    def test_web3_10(self):
        self.test_web3_9()
        self.time_test = datetime.now()

        self.driver.execute_script("window.open('about:blank','tab2')")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://mail.tandatanganku.com")

        self.input_username().send_keys("ditest6@tandatanganku.com")
        self.input_password().send_keys("ditest123" + self.keys.ENTER)
        delay(5)

        for i in range(10):
            self.refresh().click()
            delay(1.5)

        self.actions.double_click(self.msg_list_1()).perform()

        date_received = self.date_get().text
        cvrt_date_received = datetime.strptime(date_received, "%B %d, %Y %I:%M %p")

        try:
            if cvrt_date_received <= self.time_test:
                print("\nTime send documents is below than email received")
            else:
                raise Exception("\nThe message date is not more than now")
        except Exception as e:
            print(e)

        delay(2)
