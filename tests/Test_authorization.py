import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.authorization_page import AuthorizationPage
class TestAuthorization:
    names = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user", "error_user", "visual_user", "<script>", "select", "Arseniy", ""]
    my_passwords = ["secret_sauce", "secret_sa", "select", "<script>", ""]

    @classmethod
    def get_data(cls):
        return [(name, my_password) for name in cls.names for my_password in cls.my_passwords]

@pytest.fixture(autouse=True)
def setup_teardown():
    driver = webdriver.Chrome()
    with allure.step("открыть страницу https://www.saucedemo.com"):
        main_page_url = "https://www.saucedemo.com"
        driver.get(main_page_url)
    yield driver
    with allure.step("Завершить выполнение теста"):
        driver.quit()

@pytest.mark.parametrize('name, my_password', TestAuthorization.get_data())
def test_authorize(setup_teardown, name, my_password):
    driver = setup_teardown
    authorization_page = AuthorizationPage(driver)
    with allure.step(f"Найти и заполнить поле username значением: {name}"):
        authorization_page.enter_username(name)
    with allure.step(f"Найти и заполнить поле Password значением: {my_password}"):
        authorization_page.enter_password(my_password)
    with allure.step("Нажать на кнопку входа"):
        authorization_page.click_login_button()
    accept_users = {"standard_user", "locked_out_user", "problem_user", "performance_glitch_user", "error_user", "visual_user"}
    if name in accept_users and my_password == "secret_sauce":
        expected_url = "https://www.saucedemo.com/inventory.html"
    else:
        expected_url = "https://www.saucedemo.com/"
    url_after_authorization = driver.current_url
    # Проверяем успешность авторизации
    assert url_after_authorization == expected_url, "unexpected url"
