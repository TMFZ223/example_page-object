import random, pytest_check as check

import allure

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from user.user_factory import UserFactory
from config import products_list

@allure.feature("Работа со страницей товаров")
class TestProducts:

    @allure.title("Добавление случайного товара в корзину")
    def test_add_rand_product_to_cart(self, driver, login_page: LoginPage, product_page: ProductPage):
        login_page.login(UserFactory.admin())
        random_product = random.choice(products_list)
        product_page.add_products_to_cart(random_product)
        check.is_true(product_page.check_displaying_cart_counter(), "Счётчик корзины не появился")
        check.equal(product_page.check_text_cart_counter(), "1")

    @allure.title("Добавление двух товаров в корзину")
    def test_add_two_products_to_cart(self, driver, login_page: LoginPage, product_page: ProductPage):
        login_page.login(UserFactory.admin())
        product_page.add_products_to_cart(products_list[2], products_list[5])
        check.equal(product_page.check_text_cart_counter(), "2")

    @allure.title("Добавление и удаление товара из корзины")
    def test_add_and_remove_product_from_cart(self, driver, login_page: LoginPage, product_page: ProductPage):
        login_page.login(UserFactory.admin())
        random_product = random.choice(products_list)
        product_page.add_products_to_cart(random_product)
        check.equal(product_page.check_cart_link_text(), "1")
        product_page.remove_products_from_cart(random_product)
        check.equal(product_page.check_cart_link_text(), "")