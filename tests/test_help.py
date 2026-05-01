import allure
from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.HelperPage import HelpPageHelper, HelperPageLocators
from pages.AdvertisingPage import  AdvertisingPageHelper, AdvertisingPageLocators

BASE_URL = "https://ok.ru/help"

def test_help_test(browser):
    BasePage(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scroll_to_item(HelperPageLocators.ADVERTISING)
    AdvertisingPageHelper(browser)



