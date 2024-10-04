import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.authorization_page import AuthorizationPage
class TestE2E:
    names = [("standard_user"), ("Arseniy"), ("")]
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        driver = webdriver.Chrome()
        with allure.step("открыть страницу https://www.saucedemo.com"):
            main_page_url = "https://www.saucedemo.com"
            driver.get(main_page_url)
        yield driver
        with allure.step("Завершить выполнение теста"):
            driver.quit()

    @allure.description(" параметризованный тест авторизации.")
    @pytest.mark.parametrize('name', names)
    def test_authorize(self, setup_teardown, name):
        driver = setup_teardown
        authorization_page = AuthorizationPage(driver)
        with allure.step(f"Найти и заполнить поле username значением: {name}"):
            authorization_page.enter_username(name)
        with allure.step("Найти и заполнить поле Password"):
            authorization_page.enter_password('secret_sauce')
        with allure.step("Нажать на кнопку входа"):
            authorization_page.click_login_button()
        if name == "standard_user":
            expected_url = "https://www.saucedemo.com/inventory.html"
        else:
            expected_url = "https://www.saucedemo.com/"
        url_after_authorization = driver.current_url
        # Проверяем успешность авторизации
        assert url_after_authorization == expected_url, "unexpected url"