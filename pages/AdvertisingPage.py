from pages.BasePage import BasePage
import allure

class AdvertisingPageLocators:
    ADVERTISING_CABINET = ("xpath", '//span[text()="Рекламный кабинет"]')

class AdvertisingPageHelper(BasePage):
    def __init__(self,driver):
        self.driver = driver
        self.chek_page()

    def chek_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(AdvertisingPageLocators.ADVERTISING_CABINET)


