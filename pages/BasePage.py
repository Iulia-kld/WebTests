import string

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from core.BaseTest import browser


class BasePageLocators:
    LOGO = ("xpath", '//div[@class="toolbar_custom-logo_img-w"]')
    TOOLBAR_NAVICATION = ("xpath", '//span[@class="toolbar_nav_i_ic"]')
    BUTTON_MORE = ("xpath", '//a[@data-l="t,more"]')


class BasePageHelper:
    def __init__(self, driver):
        self.driver = driver

    def cheсk_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(BasePageLocators.LOGO)
        self.find_element(BasePageLocators.TOOLBAR_NAVICATION)


    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator), message=f"Не удалось найти элемент {locator}")

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_all_elements_located(locator), message=f"Не удалось найти элементы {locator}")

    @allure.step("Открываем страницу")
    def get_url(self, url):
        return self.driver.get(url)


    def attach_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), "скриншот", allure.attachment_type.PNG)

    @allure.step("Нажимаем на кнопку экосистемы vk")
    def click_button_vk_ecosystem(self):
        self.find_element(BasePageLocators.TOOLBAR_NAVICATION).click()

    @allure.step("Нажимаем на кнопку 'ещё' в экосистеме vk")
    def click_button_more(self):
        self.find_element(BasePageLocators.BUTTON_MORE).click()

    def get_window_id(self, index):
        return self.driver.window_handles[index]

    def switch_window(self, window_id):
        self.driver.switch_to.window(window_id)








