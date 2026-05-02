import allure
from core.BaseTest import browser
from pages.BasePage import BasePageHelper

class VkEcosystemPageLocators:
    LOGO_VK = ("xpath", '//a[@id="header-logo"]')
    PROJECTS = ("xpath", '//a[@class="Header_menuLink__xRXTT Header_menuLink_active__O63Dg"]')
    TITLE_LABEL = ("xpath", '//span[@class="AnimatedRows_animateItem__ztSa9 AnimatedRows_animateItemIsActive___7_2o"]')

class VkEcosystemPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.cheсk_page()

    def cheсk_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
            self.find_element(VkEcosystemPageLocators.LOGO_VK)
            self.find_element(VkEcosystemPageLocators.PROJECTS)
            self.find_element(VkEcosystemPageLocators.TITLE_LABEL)

