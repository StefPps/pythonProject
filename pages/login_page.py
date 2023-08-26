from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    _URL = "https://www.zooplus.ro/checkout/login?notLoggedIn=true"
    EMAIL_INPUT = (By.ID, "customerEmail")
    PASSWORD_INPUT = (By.ID, "customerPassword")
    LOGIN_BUTTON = (By.XPATH, "//span[text()='Intra in cont']")
    COOKIE_BUTTON = (By.ID, "onetrust-accept-btn-handler")
    NO_ACCOUNT_ERROR = (By.XPATH, "//div.v3-notigfication__text[text()='Datele de logare nu sunt corecte.']")

    # LOGIN_BUTTON = (By.CLASS_NAME, "button_group" )

    def navigate_to_page(self):
        self.driver.get(self._URL)

    def click_accept_cookie(self):
        self.click(locator=self.COOKIE_BUTTON)

    def set_email(self, email):
        self.type(locator=self.EMAIL_INPUT, text=email)

    def set_password(self, password):
        self.type(locator=self.PASSWORD_INPUT, text=password)

    def click_login(self):
        self.click(locator=self.LOGIN_BUTTON)

    def no_account_error_is_displayed(self):
        self.is_displayed(self.NO_ACCOUNT_ERROR)
