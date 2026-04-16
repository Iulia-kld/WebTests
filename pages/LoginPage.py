from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.ID, "field_email")
    PASSWORD_FIELD = (By.ID, "field_password")
    HINT_PASSWORD = ("xpath", '//button[.//span[contains(text(), "пароль")]]')
    LOGIN_BUTTON = ("xpath",  '//button[@label="Войти"]')
    LOGIN_QR_CODE_BUTTON = ("xpath",  '//button[@label="Войти по QR-коду"]')
    FAILED_LOGIN = ("xpath",  '//button[@aria-label="Не получается войти?"]')
    REGISTRATION_BUTTON = ("xpath",  '//span[contains(text(), "Зарегистрироваться")]')
    VK_ID_BUTTON = ("xpath",  '//a[@title="Войти через VK ID"]')
    MAIL_BUTTON = ("xpath",  '//a[@title="Войти через Почту"]')
    YANDEX_BUTTON = ("xpath",  '//a[@title="Войти через Яндекс"]')
    LOGIN_TAB = ("xpath",  '//a[@data-l="t,login_tab"]')
    QR_TAB = ("xpath",  '//a[@data-l="t,qr_tab"]')
    ERROR_TEXT = ("xpath", '//*[contains(@class, "error")]')


class LoginPageHelper(BasePage):
    def __init__(self,driver):
        self.driver = driver
        self.chek_page()

    def chek_page(self):
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.HINT_PASSWORD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_QR_CODE_BUTTON)
        self.find_element(LoginPageLocators.FAILED_LOGIN)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.VK_ID_BUTTON)
        self.find_element(LoginPageLocators.MAIL_BUTTON)
        self.find_element(LoginPageLocators.YANDEX_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.QR_TAB)

    def click_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    def get_error_text(self):
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    def enter_login(self):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys("AAAAAbbbbb123")