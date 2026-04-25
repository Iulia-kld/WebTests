import allure

from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper, LoginPageLocators
from pages.RecoveryPage import RecoveryPageHelper


BASE_URL = "https://ok.ru/"
LOGIN_TEXT = "email"
PASSWORD_TEXT = "12"

@allure.suite('Проверка восстановления страницы')
@allure.title('Проверка перехода к восстановлению после нескольких неудачных попыток ввести пароль')
def test_go_recovercy_after_many_fails(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.enter_login(LOGIN_TEXT)

    for i in range(3):
        LoginPage.enter_password(PASSWORD_TEXT)
        LoginPage.click_login()

    LoginPage.click_recovery()
    RecoveryPageHelper(browser)




