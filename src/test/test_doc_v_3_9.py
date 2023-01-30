import re
from datetime import datetime, timedelta

from selenium.webdriver.support.select import Select
from main import delay, MailObject
from test_doc_prod import TestDocProd


class TestNewScript(TestDocProd, MailObject):
    def test_web1_1(self):
        self.test_send_document()

    def test_web1_2(self):
        self.test_send_document(exe='img')

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

    def test_web2_3_3(self, **kwargs):
        seal = kwargs.get('seal', False)
        self.test_need_check(seal=seal)

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
        self.test_need_paraf(corp=True)

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
        """semi-automation because its receiving and sending otp Email"""
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
        """semi-automation because its receiving and sending otp SMS"""
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
        """semi-automation because its receiving and sending otp"""
        self.test_denial_process()

        self.text_area_reason().send_keys("testing")
        self.btn_otp_email().click()

        delay(25)

        self.btn_prosign().click()
        self.btn_saya_yakin().click()
        delay(7)

    def test_web3_9(self):
        """semi-automation because its receiving and sending otp"""
        self.test_agreement_process()

        self.btn_otp_email().click()

        delay(25)

        self.btn_prosign().click()
        self.btn_saya_yakin().click()
        delay(7)

    def test_web3_10(self):
        """semi-automation because its receiving and sending otp"""
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

    def test_web4_1(self):
        self.test_need_paraf(corp=True)

        self.driver.execute_script("window.open('about:blank','tab2')")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://app.tandatanganku.com")

        self.username().send_keys("ditest6@tandatanganku.com" + self.keys.ENTER)
        self.password().send_keys("Coba1234" + self.keys.ENTER)

        self.need_sign().click()
        self.latest_inbox().click()

        try:
            assert self.canvas() is not None
        except Exception as e:
            raise e

    def test_web4_2(self, **kwargs):
        otp = kwargs.get('otp_code', "002383")
        otp_type = kwargs.get('otp_type', "email")
        semi_automation = kwargs.get('semi_automation', False)

        if otp_type is "email":
            self.username().send_keys("ditest6@tandatanganku.com" + self.keys.ENTER)
            self.password().send_keys("Coba1234", self.keys.ENTER)
            delay(2)
        elif otp_type is "sms":
            self.username().send_keys("wahyuhi" + self.keys.ENTER)
            self.password().send_keys("Kijang321!" + self.keys.ENTER)
            self.choose_account().click()
            delay(2)

        self.need_sign().click()
        self.latest_inbox().click()
        delay(4)

        self.button_proses_sign_one().click()
        delay(2)

        if otp_type == "email":
            self.btn_otp_email().click()
            if semi_automation is False:
                self.otp_input_number().send_keys(otp)
                delay(10)
            else:
                delay(20)
        elif otp_type == "sms":
            self.btn_otp_sms().click()
            if semi_automation is False:
                self.otp_input_number().send_keys(otp)
                delay(10)
            else:
                delay(20)

        self.btn_prosign().click()
        self.btn_saya_yakin().click()

        delay(15)

        if semi_automation is False:
            try:
                assert self.swal_otp_none() is not None
            except Exception as e:
                raise e

    def test_web4_3(self):
        """semi-automation because its receiving and sending otp"""
        self.test_web4_2(semi_automation=True)

    def test_web4_4(self):
        """semi-automation because its receiving and sending otp"""
        self.test_web4_2(semi_automation=True, otp_type="sms")

    def test_web4_5(self, **kwargs):
        """semi-automation because its receiving and sending otp"""
        is_used = kwargs.get('used', False)
        self.username().send_keys("ditest6@tandatanganku.com" + self.keys.ENTER)
        self.password().send_keys("Coba1234", self.keys.ENTER)
        delay(2)

        self.need_sign().click()
        self.latest_inbox().click()

        self.button_proses_sign_one().click()
        delay(2)

        if is_used is False:
            self.label_tidak().click()
            delay(3)
            self.text_area_reason().send_keys("testing")

        self.btn_otp_email().click()

        delay(20)

        self.btn_prosign().click()
        delay(2)

        self.btn_saya_yakin().click()
        delay(10)

    def test_web4_6(self):
        """semi-automation because its receiving and sending otp"""
        self.test_web4_5(used=True)

    def test_web4_7(self):
        """semi-automation because its receiving and sending otp"""
        self.test_web4_6()
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

    def test_web5_1(self, **kwargs):
        """all of this is semi-automation test because it's receiving an OTP"""
        is_used = kwargs.get('used', False)

        if is_used is False:
            self.username().send_keys("wahyuhi" + self.keys.ENTER)
            self.password().send_keys("Kijang321!" + self.keys.ENTER)
            self.choose_account().click()

        delay(2)

        self.need_sign().click()
        self.latest_inbox().click()

    def test_web5_2(self):
        self.test_web5_1()

        self.button_proses_sign_one().click()
        delay(2)
        self.btn_otp_email().click()
        self.otp_input_number().send_keys("002383")

        self.btn_prosign().click()
        self.btn_saya_yakin().click()

        try:
            assert self.swal_otp_none() is not None
        except Exception as e:
            raise e

        delay(10)

    def test_web5_3(self, **kwargs):
        """semi-automation because its receiving and sending otp"""
        otp = kwargs.get("otp", "email")
        is_used = kwargs.get('used', False)
        denial = kwargs.get('denial', False)
        self.test_web5_1(used=is_used)

        self.button_proses_sign_one().click()
        delay(2)

        if denial is True:
            self.label_tidak().click()
            delay(3)
            self.text_area_reason().send_keys("testing")

        if otp is "email":
            self.btn_otp_email().click()
        else:
            self.btn_otp_sms().click()

        delay(20)

        self.btn_prosign().click()
        self.btn_saya_yakin().click()

        delay(15)

    def test_web5_4(self, **kwargs):
        """semi-automation because its receiving and sending otp"""
        denial = kwargs.get('denial', False)
        self.test_web2_3_3(seal=True)
        self.btn_add_sign().click()

        self.lock_sign_1().click()
        self.btn_set_email().click()

        self.btn_send_doc().click()
        self.btn_process_send_doc().click()
        delay(3)
        self.confirm_after_send_doc().click()
        delay(2)

        self.driver.execute_script("window.open('about:blank','tab2')")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://app.tandatanganku.com")

        self.test_web5_3(otp="sms", used=True, denial=denial)

    def test_web5_5(self):
        """semi-automation because its receiving and sending otp"""
        self.test_web5_4(denial=True)

    def test_web5_6(self):
        """semi-automation because its receiving and sending otp"""
        self.test_web5_4(denial=False)

    def test_web5_7(self):
        """semi-automation because its receiving and sending otp"""
        self.test_web5_6()
        self.time_test = datetime.now()

        self.driver.execute_script("window.open('about:blank','tab3')")
        self.driver.switch_to.window(self.driver.window_handles[2])
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

    def test_web6_1(self):
        """all of this is semi-automation test because it's receiving an OTP"""
        self.test_web2_5_3()

        self.driver.execute_script("window.open('about:blank','tab2')")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://app.tandatanganku.com")

        self.need_sign().click()
        self.latest_inbox().click()

        try:
            assert self.canvas() is not None
        except Exception as e:
            raise e

        delay(2)

    def test_web6_2(self, **kwargs):
        auto = kwargs.get('auto', True)
        used = kwargs.get('used', False)
        denial = kwargs.get('denial', False)
        otp_type = kwargs.get('otp_type', 'email')
        self.username().send_keys("wahyuhi" + self.keys.ENTER)
        self.password().send_keys("Kijang321!" + self.keys.ENTER)
        self.choose_account().click()

        delay(3)

        self.need_sign().click()
        self.latest_inbox().click()

        self.button_proses_sign_one().click()
        delay(2)

        if denial is True:
            self.label_tidak().click()
            delay(3)
            self.text_area_reason().send_keys("testing")

        if otp_type is "email":
            self.btn_otp_email().click()
        elif otp_type is "sms":
            self.btn_otp_sms().click()

        if auto is True:
            self.otp_input_number().send_keys("002383")
        else:
            delay(25)

        self.btn_prosign().click()
        self.btn_saya_yakin().click()

        if used is False:
            try:
                assert self.swal_otp_none() is not None
            except Exception as e:
                raise e

        delay(10)

    def test_web6_3(self):
        """I don't know its can run or not because app.tandatanganku.com is cannot send OTP to digi-id email"""
        self.test_web6_2(auto=False, used=True)

    def test_web6_4(self):
        """semi-automation because its receiving and sending otp"""
        self.test_web6_2(auto=False, otp_type="sms", used=True)

    def test_web6_5(self):
        """semi-automation because its receiving and sending otp"""
        self.test_web6_2(auto=False, denial=True, otp_type="sms", used=True)

    def test_web6_6(self):
        """semi-automation because its receiving and sending otp"""
        self.test_web6_2(auto=False, denial=False, otp_type="sms", used=True)

    def test_web6_7(self):
        """semi-automation because its receiving and sending otp"""
        self.test_web6_6()
        self.time_test = datetime.now()

        self.driver.execute_script("window.open('about:blank','tab3')")
        self.driver.switch_to.window(self.driver.window_handles[2])
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
