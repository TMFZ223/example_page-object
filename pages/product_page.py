import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait

from locators.products_page_locators import ProductPageLocators
from pages.base_page import BasePage

class ProductPage(BasePage):
    locators = ProductPageLocators()

    @allure.step("Проверить наличие заголовка страницы")
    def check_displaying_title(self):
        return self.element_is_visible(self.locators.page_title).is_displayed()

    @allure.step("Проверить текст заголовка страницы")
    def check_title(self):
        return self.element_is_visible(self.locators.page_title).text

    @allure.step("Добавить в корзину следующие товары: {products}")
    def add_products_to_cart(self, *products):
        pattern = self.locators.ADD_TO_CART_PATTERN
        for product in products:
            locator = (By.XPATH, pattern.format(product))
            self.element_is_visible(locator).click()

    @allure.step("Удалить из корзины следующие товары: {products}")
    def remove_products_from_cart(self, *products):
        pattern = self.locators.REMOVE_PATTERN
        for product in products:
            locator = (By.XPATH, pattern.format(product))
            self.element_is_visible(locator).click()

    @allure.step("Убедиться в наличии счётчика корзины")
    def check_displaying_cart_counter(self):
        return self.element_is_visible(self.locators.cart_counter).is_displayed()

    @allure.step("Проверить состояние счётчика корзины")
    def check_text_cart_counter(self):
        return self.element_is_visible(self.locators.cart_counter).text

    @allure.step("Проверить текст ссылки перехода в корзину")
    def check_cart_link_text(self):
        return self.element_is_visible(self.locators.cart_link).text