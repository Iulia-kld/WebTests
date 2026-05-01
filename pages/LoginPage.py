import allure

from pages.BasePage import BasePageHelper
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
    CANCEL_BUTTON = ("xpath", '//span[contains(text(), "Отмена")]')
    RESTORE_BUTTON = ("xpath", '//a//span[contains(text(), "Восстановить")]')



class LoginPageHelper(BasePageHelper):
    def __init__(self,driver):
        self.driver = driver
        self.cheсk_page()

    def cheсk_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
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

    @allure.step("Нажимаем на кнопку 'Войти'")
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step("Получаем текст ошибки")
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step("Вводим значение в поле 'Логин'")
    def enter_login(self, login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()

    @allure.step("Вводим значение в поле 'Пароль'")
    def enter_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    @allure.step("Кликаем на кнопку 'Восстановить'")
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.RESTORE_BUTTON).click()

    @allure.step("Кликаем на кнопку 'Далее' на странице регистрации")
    def click_registration(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON).click()


