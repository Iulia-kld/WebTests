import allure
from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.HelperPage import HelpPageHelper, HelperPageLocators
from pages.AdvertisingPage import  AdvertisingPageHelperHelper, AdvertisingPageLocators

BASE_URL = "https://ok.ru/help"

def test_help_test(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scroll_to_item(HelperPageLocators.ADVERTISING)
    AdvertisingPageHelperHelper(browser)



