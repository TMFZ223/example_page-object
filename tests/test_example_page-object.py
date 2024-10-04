import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.authorization_page import AuthorizationPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.order_page import OrderPage
from pages.finish_order_page import FinishOrderPage

class TestE2E:
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        driver = webdriver.Chrome()
        with allure.step("открыть страницу https://www.saucedemo.com"):
            main_page_url = "https://www.saucedemo.com"
            driver.get(main_page_url)
        yield driver
        with allure.step("Завершить выполнение теста"):
            driver.quit()

    @allure.description("E2E test. Данный тест демонстрирует работу сайта магазина товаров (от авторизации до оформления заказа).")
    def test_shopping(self, setup_teardown):
        driver = setup_teardown
        authorization_page = AuthorizationPage(driver)
        with allure.step("Найти и заполнить поле username"):
            authorization_page.enter_username('standard_user')
        with allure.step("Найти и заполнить поле Password"):
            authorization_page.enter_password('secret_sauce')
        with allure.step("Нажать на кнопку входа"):
            authorization_page.click_login_button()
        url_after_authorization = driver.current_url
        # Проверяем успешность авторизации
        assert 'https://www.saucedemo.com/inventory.html' in url_after_authorization, "authorization failed"
        product_page = ProductPage(driver)
        with allure.step("Выбрать товар Sauce Labs Backpack"):
            product_page.choose_product()
        with allure.step("Добавить выбранный товар в корзину"):
            product_page.add_product_to_cart()
        cart_page = CartPage(driver)
        with allure.step("Перейти в корзину с добавленным товаром"):
            cart_page.go_cart()
        actual_product_in_my_cart = driver.find_element(By.XPATH, "//div[@class ='inventory_item_name']")
        assert actual_product_in_my_cart.text == 'Sauce Labs Backpack', "Problems adding product to cart"
        order_page = OrderPage(driver)
        with allure.step("Нажать на кнопку для начала оформления заказа"):
            order_page.click_buy_button()
        with allure.step("Заполнить поле firstname"):
            order_page.enter_firstname('Testname')
        with allure.step("Заполнить поле lastname"):
            order_page.enter_lastname('learnqa')
        with allure.step("Заполнить поле zip_postal_cod"):
            order_page.enter_zip_postal_cod('125212')
        with allure.step("Нажать на кнопку для продолжения заказа"):
            order_page.click_next_button()
        finish_order_page = FinishOrderPage(driver)
        with allure.step("Нажать на кнопку для завершения заказа"):
            finish_order_page.click_finish_button()
        actual_header = driver.find_element(By.XPATH, "//h2[@class ='complete-header']") # поиск элемента успешного оформления покупки
        expected_result = 'Thank you for your order!' # Ожидаемый текст заголовка после успешной покупки
        actual_result = actual_header.text # Фактический результат
        assert actual_result == expected_result, "actual_result doesn't look like expected_result"