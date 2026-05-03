from selenium.webdriver import ActionChains
from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
import allure

class HelperPageLocators:

    LOGIN_BUTTON_TOOLBAR = ("xpath", '//div[@class="anon-tb-login"]')
    BUTTON_TO_SEARCH = ("xpath", '//span[@data-tsid="button_to_search"]')
    INPUT_SEARCH = ("xpath", '//input[@type="search"]')
    ACTUAL_TODAY = ("xpath", '//a[contains(@href, "segodnya-aktualno")]')
    REGISTRATION = ("xpath", '//a[contains(@href, "registraciya")]')
    MY_PROFILE= ("xpath", '//a[contains(@href, "moi-profil")]')
    COMMUNICATION = ("xpath", '//a[contains(@href, "obshchenie")]')
    ACCESS_TO_PROFILE = ("xpath", '//a[contains(@href, "dostup-k-profilu")]')
    SECURITY = ("xpath", '//a[contains(@href, "bezopasnost")]')
    GROOPS = ("xpath", '//a[contains(@href, "gruppy")]')
    PAID_FUNCTIONS = ("xpath", '//a[contains(@href, "platnye-funkcii")]')
    SPAM = ("xpath", '//a[contains(@href, "narusheniya-i-spam")]')
    GAMES = ("xpath", '//a[contains(@href, "igry-i-prilojeniya")]')
    SERVISES = ("xpath", '//a[contains(@href, "drugie-servisy")]')
    INFORMATION = ("xpath", '//a[contains(@href, "poleznaya-informaciya")]')
    ADVERTISING = ("xpath", '//a[contains(@href, "reklamnyi-kabinet")]')

class HelpPageHelper(BasePageHelper):
    def __init__(self,driver):
        self.driver = driver
        self.cheсk_page()

    def cheсk_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(HelperPageLocators.LOGIN_BUTTON_TOOLBAR)
        self.find_element(HelperPageLocators.BUTTON_TO_SEARCH)
        self.find_element(HelperPageLocators.INPUT_SEARCH)
        self.find_element(HelperPageLocators.ACTUAL_TODAY)
        self.find_element(HelperPageLocators.REGISTRATION)
        self.find_element(HelperPageLocators.MY_PROFILE)
        self.find_element(HelperPageLocators.COMMUNICATION)
        self.find_element(HelperPageLocators.ACCESS_TO_PROFILE)
        self.find_element(HelperPageLocators.SECURITY)
        self.find_element(HelperPageLocators.GROOPS)
        self.find_element(HelperPageLocators.PAID_FUNCTIONS)
        self.find_element(HelperPageLocators.SPAM)
        self.find_element(HelperPageLocators.GAMES)
        self.find_element(HelperPageLocators.SERVISES)
        self.find_element(HelperPageLocators.INFORMATION)
        self.find_element(HelperPageLocators.ADVERTISING)

    def scroll_to_item(self, locator):
        scroll_item = self.find_element(locator)
        ActionChains(self.driver).scroll_to_element(scroll_item).click(scroll_item).perform()