import allure

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class RecoveryPageLocators:
    PHONE_BUTTON = ("xpath", '//a[@data-l="t,phone"]')
    EMAIL_BUTTON = ("xpath", '//a[@data-l="t,email"]')
    QA_CODE = ("xpath", '//*[@class="qr_code_image"]')
    SUPPORT_LINK = ("xpath", '//*[@data-l="t,support"]')


class RecoveryPageHelper(BasePage):
    def __init__(self,driver):
        self.driver = driver
        self.chek_page()

    def chek_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(RecoveryPageLocators.PHONE_BUTTON)
        self.find_element(RecoveryPageLocators.EMAIL_BUTTON)
        self.find_element(RecoveryPageLocators.QA_CODE)
        self.find_element(RecoveryPageLocators.SUPPORT_LINK)


