import random, pytest_check as check

import allure
from enums.page_titles import PageTitle
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from user.user_factory import UserFactory
from config import products_list

@allure.feature("Работа со страницей корзины")
class TestCart:

    @allure.title("Переход в корзину")
    def test_go_cart(self, driver, login_page: LoginPage, product_page: ProductPage, cart_page: CartPage):
        login_page.login(UserFactory.admin())
        product_page.go_cart()
        check.is_true(cart_page.check_displaying_title(), "Заголовок не появился")
        check.equal(cart_page.check_title(), PageTitle.CART.value)

    @allure.title("Добавление и просмотр добавленного товара в корзине")
    def test_add_to_cart_and_display_product(self, driver, login_page: LoginPage, product_page: ProductPage, cart_page: CartPage):
        login_page.login(UserFactory.admin())
        random_product = random.choice(products_list)
        product_page.add_products_to_cart(random_product)
        product_page.go_cart()
        products = cart_page.get_cart_products_list()
        check.equal(len(products), 1)
        check.is_true(random_product in products, f"Товары в корзине: {products})

    @allure.title("Продолжение покупок после добавления товара в корзину")
    def test_continue_shopping_after_add_product_to_cart(self, driver, login_page: LoginPage, product_page: ProductPage, cart_page: CartPage):
        login_page.login(UserFactory.admin())
        product_page.add_products_to_cart(products_list[1])
        product_page.go_cart()
        cart_page.click_continue_shopping_button()
        product_page.add_products_to_cart(products_list[4])
        product_page.go_cart()
        products = cart_page.get_cart_products_list()
        check.equal(len(products), 2)
        check.is_true(products_list[1] in products and products_list[4] in products, f"Товары в корзине: {products}")