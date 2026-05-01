from pages.BasePage import BasePageHelper
import allure

class AdvertisingPageLocators:
    ADVERTISING_CABINET = ("xpath", '//span[text()="Рекламный кабинет"]')

class AdvertisingPageHelperHelper(BasePageHelper):
    def __init__(self,driver):
        self.driver = driver
        self.cheсk_page()

    def cheсk_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(AdvertisingPageLocators.ADVERTISING_CABINET)


