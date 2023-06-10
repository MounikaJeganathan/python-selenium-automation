from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignIn(Page):
    SIGN_IN_HEADER = (By.CSS_SELECTOR, "h1.a-spacing-small")
    EMAIL_FIELD = (By.ID, 'ap_email')

    def sigin_header(self):
        self.verify_is_displayed(*self.SIGN_IN_HEADER)
        print("Sign in Page loaded sucessfully ")

    def email_field(self):
        self.verify_is_displayed(*self.EMAIL_FIELD)
        print("Email field is displayed")
