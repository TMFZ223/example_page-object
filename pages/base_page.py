import allure
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from locators.base_locators import BaseLocators

class BasePage:
    locators = BaseLocators()
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)

    def element_is_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Проверить наличие заголовка страницы")
    def check_displaying_title(self):
        return self.element_is_visible(self.locators.page_title).is_displayed()

    @allure.step("Проверить текст заголовка страницы")
    def check_title(self):
        return self.element_is_visible(self.locators.page_title).text
