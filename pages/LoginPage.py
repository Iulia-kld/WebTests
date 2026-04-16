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


class LoginPageHelper(BasePage):
    pass