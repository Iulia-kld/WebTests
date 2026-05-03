import allure
from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageLocators, LoginPageHelper
from pages.VkEcosystem import VkEcosystemPageHelper, VkEcosystemPageLocators

BASE_URL = "https://ok.ru/"

@allure.suite('Проверка тулбара')
@allure.title('Переход к проектам экосистемы VK')
def test_open_ecosystem(browser):
    BasePage = BasePageHelper(browser)
    BasePage.get_url(BASE_URL)
    BasePage.cheсk_page()
    LoginPage = LoginPageHelper(browser)
    current_window_id = LoginPage.get_window_id(0)
    LoginPage.click_button_vk_ecosystem()
    LoginPage.click_button_more()
    new_window_id = LoginPage.get_window_id(1)
    LoginPage.switch_window(new_window_id)
    VkEcosystemPage = VkEcosystemPageHelper(browser)
    VkEcosystemPage.switch_window(current_window_id)
    LoginPageHelper(browser)