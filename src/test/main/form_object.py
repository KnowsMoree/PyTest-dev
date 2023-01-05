import main


class FormObject(main.TestWebsite):
    def link_reg(self):
        return self.driver.find_element(self.by.XPATH, "/html/body/div/div/div/div[1]/div[2]/div[1]/a[1]")

    def username(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='username']")

    def password(self):
        return self.driver.find_element(self.by.XPATH, "//input[@id='pd']")

    def saldo_sign(self):
        return self.driver.find_element(self.by.XPATH, "/html/body/div[1]/div[2]/div[2]/div[11]/div[3]/div/div/div")

    def nik_input(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='idcard']")

    def password_submit(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='submit']")

    def doc_file(self):
        return self.driver.find_element(self.by.XPATH, "//input[@type='file']")

    def btn_input_file(self):
        return self.driver.find_element(self.by.XPATH, "//span[@class='btn btn-danger ']")

    def doc_submit(self):
        return self.driver.find_element(self.by.XPATH, "//button[@type='submit']")

    def password_salah(self):
        return self.driver.find_element(self.by.XPATH, "//div[@class='alert alert-danger']")

    def error_username(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='e_username']")

    def pass_error(self):
        return self.driver.find_element(
            self.by.XPATH, "//*[text() = '[Password salah sebanyak 3x. Silakan coba kembali setelah 10 menit.]']")

    def error_format16_nik(self):
        return self.driver.find_element(
            self.by.XPATH, "//div[@id = 'e_idcard' and (text() = 'Harus 16 Digit.' or . = 'Harus 16 Digit.')]")

    def error_format_false(self):
        return self.driver.find_element(self.by.XPATH, "//*[text() = 'Format NIK Salah']")

    def birth_place_input(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='lbrith']")

    def btn_next_step1(self):
        return self.driver.find_element(self.by.XPATH, "//button[@onclick='step1()']")

    def validation_name(self):
        return self.driver.find_element(
            self.by.XPATH, "//input[@id='name'][contains(@class,'form-control input-md is-invalid')]")

    def name_input(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='name']")

    def gender_select(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='jk']")

    def validation_place(self):
        return self.driver.find_element(
            self.by.XPATH, "//input[@id='lbrith'][@class='form-control input-md is-invalid']")

    def step2(self):
        return self.driver.find_element(self.by.XPATH, "//*[text() = 'Informasi Akun']")

    def password_reg(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='password']")

    def password_confirmation(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='password2']")

    def email_input_register(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='email']")

    def phone_input_register(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='handphone']")

    def step3(self):
        return self.driver.find_element(self.by.XPATH, "//button[@onclick='step3()']")

    def validation_username(self):
        return self.driver.find_element(
            self.by.XPATH, "//input[@id='username'][@class='form-control input-md is-invalid']")

    def err_username(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='e_username']")

    def username_registered(self):
        return self.driver.find_element(self.by.XPATH, "/html/body/div[11]/form/div/div[4]/div[1]/div/div[2]/i")

    def password_too_short(self):
        return self.driver.find_element(self.by.XPATH, "//*[text() = 'Password terlalu pendek, min 8 character']")

    def password_minus_symbol(self):
        return self.driver.find_element(
            self.by.XPATH, "//*[text() = 'Password harus mengandung minimal 1 Simbol/Karakter Spesial']")

    def strong_password(self):
        return self.driver.find_element(self.by.XPATH, "//*[text() = 'Strong password']")

    def pass_not_same(self):
        return self.driver.find_element(self.by.XPATH, "//*[@id='e_password2']")

    def validation_email(self):
        return self.driver.find_element(
            self.by.XPATH, "//input[@id='email'][@class='form-control input-md is-invalid']")

    def email_taken(self):
        return self.driver.find_element(self.by.XPATH, "//*[text() = 'Email sudah terdaftar gunakan email lain']")

    def number_taken(self):
        return self.driver.find_element(
            self.by.XPATH,
            "//div[@id = 'e_handphone' and (text() = 'No HP sudah terdaftar gunakan nomor lain' or . = 'No HP sudah terdaftar gunakan nomor lain')]")

    def email_invalid(self):
        return self.driver.find_element(self.by.XPATH, "//*[text() = 'Invalid Email Address']")

    def number_invalid(self):
        return self.driver.find_element(
            self.by.XPATH, "//input[@id='handphone'][@class='NumOnly form-control input-md is-invalid']")

    def false_number_format(self):
        return self.driver.find_element(self.by.XPATH, "//*[text() = 'Format nomor salah']")

    def number_less_than_8(self):
        return self.driver.find_element(self.by.XPATH, "//*[text() = 'Nomor HP Minimal 8 digit']")

    def step3_title(self):
        return self.driver.find_element(
            self.by.XPATH, "//h3[(text() = 'Foto dan Tandatangan' or . = 'Foto dan Tandatangan')]")

    def ktp_input(self):
        return self.driver.find_element(self.by.XPATH, "//input[@type='file']")

    def span_ktp_input(self):
        return self.driver.find_element(self.by.XPATH, "//span[.//*[@id='imgektp']]")
