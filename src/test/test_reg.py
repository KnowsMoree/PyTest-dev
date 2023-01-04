import main


class TestReg(main.TestWebsite):
    def test_reg_page(self):
        self.reg_and_log_object("link_reg").click()
        main.delay(3)

    def test_reg_nik(self):
        self.reg_and_log_object("link_reg").click()
        main.delay(0.5)
        self.reg_and_log_object("nik_input").send_keys("8928839489849203")
        main.delay(3)

    def test_format16_nik(self):
        self.test_reg_page()

        self.reg_and_log_object("nik_input").send_keys("920390239239")
        main.delay(0.5)
        assert self.reg_and_log_object("error_format16_nik") is not None
        main.delay(2)

    def test_format_false(self):
        self.test_reg_page()

        self.reg_and_log_object("nik_input").send_keys("0")
        main.delay(0.5)
        assert self.reg_and_log_object("error_format_false") is not None
        main.delay(2)

    def test_cant_input_string(self):
        self.test_reg_page()

        self.reg_and_log_object("nik_input").send_keys("a")
        main.delay(0.5)

        assert self.reg_and_log_object("error_format16_nik") is not None

    def test_nik_registered(self):
        self.test_reg_page()

        self.reg_and_log_object("nik_input").send_keys("3275025302090003")
        main.delay(0.5)
        self.reg_and_log_object("birth_place_input").send_keys("jakarta")
        self.reg_and_log_object("btn_next_step1").click()

        assert self.reg_and_log_object("validation_name") is not None

    def test_birth_place_validation(self, **kwargs):
        is_use = kwargs.get("use", False)
        self.test_reg_page()

        self.reg_and_log_object("nik_input").send_keys("3275025302090003")
        main.delay(0.5)
        self.reg_and_log_object("name_input").send_keys("mimio")

        main.Select(self.reg_and_log_object("gender_select")).select_by_visible_text("Perempuan")
        main.delay(5)

        if is_use:
            self.reg_and_log_object("birth_place_input").send_keys("jakarta")
            main.delay(5)
            self.reg_and_log_object("btn_next_step1").click()
        else:
            self.reg_and_log_object("btn_next_step1").click()
            main.delay(5)
            assert self.reg_and_log_object("validation_place") is not None

    def test_full_identity(self):
        self.test_birth_place_validation(use=True)
        main.delay(3)

        assert self.reg_and_log_object("step2") is not None

    def test_empty_username(self):
        self.test_birth_place_validation(use=True)

        self.reg_and_log_object("password_reg").send_keys("asdf1234!")
        self.reg_and_log_object("password_confirmation").send_keys("asdf1234!")

        self.reg_and_log_object("email_input_register").send_keys("testing223@spambox.xyz")
        self.reg_and_log_object("phone_input_register").send_keys("89237738883")

        self.reg_and_log_object("step3").click()
        main.delay(3)
        assert self.reg_and_log_object("validation_username") is not None

    def test_minus_characters_username(self):
        self.test_birth_place_validation(use=True)
        self.reg_and_log_object("uname").send_keys("asd")
        main.delay(1)

        assert self.reg_and_log_object("err_username") is not None
        main.delay(1.5)

    def test_username_registered(self):
        self.test_birth_place_validation(use=True)

        self.reg_and_log_object("uname").send_keys("wahyuhidy")
        main.delay(1)

        assert self.reg_and_log_object("username_registered") is not None
        main.delay(1.5)

    def test_password_too_short(self):
        self.test_birth_place_validation(use=True)

        self.reg_and_log_object("password_reg").send_keys("hi!23")
        main.delay(3)
        assert self.reg_and_log_object("password_too_short") is not None
        main.delay(1)

    def test_minus_symbol_pass(self):
        self.test_birth_place_validation(use=True)

        self.reg_and_log_object("password_reg").send_keys("asda")
        main.delay(2)
        assert self.reg_and_log_object("password_minus_symbol") is not None

    def test_strong_password(self):
        self.test_birth_place_validation(use=True)

        self.reg_and_log_object("password_reg").send_keys("Mamang123!")
        main.delay(2)

        assert self.reg_and_log_object("strong_password") is not None

    def test_password_is_not_same(self):
        self.test_birth_place_validation(use=True)

        self.reg_and_log_object("password_reg").send_keys("Mamang123!")
        self.reg_and_log_object("password_confirmation").send_keys("Mam2131")

        main.delay(2)

        assert self.reg_and_log_object("pass_not_same") is not None

    def test_email_validation(self):
        self.test_birth_place_validation(use=True)

        self.reg_and_log_object("uname").send_keys("kijang")
        self.reg_and_log_object("password_reg").send_keys("Mamang123!")
        self.reg_and_log_object("password_confirmation").send_keys("Mam2131")
        self.reg_and_log_object("phone_input_register").send_keys("89773827839")

        self.reg_and_log_object("step3").click()
        main.delay(2)

        assert self.reg_and_log_object("validation_email") is not None

    def test_email_taken(self, **kwargs):
        email = kwargs.get("email", "ditest10@tandatanganku.com")
        test_obj = kwargs.get("obj", "email_taken")
        self.test_birth_place_validation(use=True)
        main.delay(2)
        self.reg_and_log_object("email_input_register").send_keys(email)
        main.delay(3)

        assert self.reg_and_log_object(test_obj) is not None

    def test_invalid_email(self):
        self.test_email_taken(obj="email_invalid", email="asdas")

    def test_invalid_number(self):
        self.test_birth_place_validation(use=True)

        self.reg_and_log_object("step3").click()
        main.delay(2)
        assert self.reg_and_log_object("number_invalid") is not None

    # def test_number_taken(self):
    #     self.test_birth_place_validation(use=True)

    def test_false_format_number(self):
        self.test_birth_place_validation(use=True)

        self.reg_and_log_object("phone_input_register").send_keys("09123")
        main.delay(1)
        assert self.reg_and_log_object("false_number_format") is not None

    def test_number_less_than_8(self):
        self.test_birth_place_validation(use=True)

        self.reg_and_log_object("phone_input_register").send_keys("892")
        main.delay(1)

        assert self.reg_and_log_object("number_less_than_8") is not None

    def test_true_identity(self, **kwargs):
        redundancy = kwargs.get("redundancy", False)
        self.test_birth_place_validation(use=True)

        self.reg_and_log_object("uname").send_keys("asdteuse782")
        main.delay(2)
        self.reg_and_log_object("password_reg").send_keys("Mamang123!")
        self.reg_and_log_object("password_confirmation").send_keys("Mamang123!")
        self.reg_and_log_object("email_input_register").send_keys("amang78@spambox.xyz")
        self.reg_and_log_object("phone_input_register").send_keys("894381216")

        main.delay(5)
        self.actions.double_click(self.reg_and_log_object("step3")).perform()

        if redundancy:
            pass
        else:
            assert self.reg_and_log_object("step3_title") is not None

    def test_input_ktp(self):
        self.test_true_identity(redundancy=True)

        main.delay(2)
        self.reg_and_log_object("span_ktp_input").click()
        main.delay(4)
        # self.robot.keyUp("escape")
        # self.robot.keyDown("escape")
        self.robot.press("escape")
        main.delay(2)
        self.reg_and_log_object("ktp_input").send_keys(
            "C:\\Users\\dignitas\\Downloads\\npwp_20221101055126 (1).jpg")
        main.delay(5)
