import allure
from locators.cart_page_locators import CartPageLocators
from pages.base_page import BasePage

class CartPage(BasePage):
    locators = CartPageLocators()


    @allure.step("Получить список товаров, добавленных в корзину")
    def get_cart_products_list(self) -> list[str]:
        elements = self.elements_are_visible(self.locators.cart_product)
        return [product.text for product in elements]

    @allure.step("Нажать на кнопку продолжения покупок")
    def click_continue_shopping_button(self):
        self.element_is_visible(self.locators.continue_shopping).click()