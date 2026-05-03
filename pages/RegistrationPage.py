import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
import random

class RegistrationPageLocators:

    ABOUT_VK_LINK = ("xpath", '//span[contains(text(), "VK")]')
    LICENSE_AGREEMENT_LINK = ("xpath", '//a[@data-test-id="agreement-link-0"]')
    PRIVACY_POLICY = ("xpath", '//a[@data-test-id="agreement-link-1"]')
    NEXT_BUTTON = ("xpath", '//button[contains(@class, "vkuiButton__modePrimary")]')
    PHONE_ENTER_FIELD = ("xpath", '//input[@type="tel"]')
    COUNTRY_DROPDOWN = ("xpath", '//button[@aria-label="Страна или код"]')
    COUNTRY_ITEMS = ("xpath", '//div[contains(@class, "CountryList-module_countryList__listItem__bflkV")]')


class RegistrationPageHelper(BasePageHelper):
    def __init__(self,driver):
        self.driver = driver
        self.cheсk_page()

    def cheсk_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(RegistrationPageLocators.ABOUT_VK_LINK)
        self.find_element(RegistrationPageLocators.LICENSE_AGREEMENT_LINK)
        self.find_element(RegistrationPageLocators.NEXT_BUTTON)
        self.find_element(RegistrationPageLocators.PHONE_ENTER_FIELD)
        # self.find_element(RegistrationPageLocators.COUNTRY_ITEMS)
        self.find_element(RegistrationPageLocators.COUNTRY_DROPDOWN)

    def select_random_country(self):
        self.find_element(RegistrationPageLocators.COUNTRY_DROPDOWN).click()
        country_items = self.find_elements(RegistrationPageLocators.COUNTRY_ITEMS)
        random_number = random.randint(0, len(country_items) - 1)
        selected_country = country_items[random_number]
        country_code = selected_country.text.split("\n")[1]
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            selected_country
        )
        selected_country.click()
        return country_code

    def get_phone_field_value(self):
        return self.find_element(RegistrationPageLocators.PHONE_ENTER_FIELD).get_attribute('value').strip()
