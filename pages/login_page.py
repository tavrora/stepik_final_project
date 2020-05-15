from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    """Class for working with the login (inherited from the base)"""
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert "login" in self.url, \
            "The word 'login' is not contained in the current url"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not presented"

    def register_new_user(self, email, password):
        # найти поле почты и вставить туда email
        field_email = self.browser.find_element(*LoginPageLocators.FIELD_EMAIL)
        field_email.send_keys(email)
        # найти поле пароля и вставить туда password
        field_email = self.browser.find_element(*LoginPageLocators.FIELD_PASSWORD)
        field_email.send_keys(password)
        # найти поле подтверждения пароля и вставить туда password
        field_email = self.browser.find_element(*LoginPageLocators.FIELD_PASSWORD_CONFIRM)
        field_email.send_keys(password)
        # нажать кнопку "зарегистрироваться"
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()