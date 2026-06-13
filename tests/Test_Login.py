import allure
import pytest
import pytest_check as check
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from user.user_factory import UserFactory
from enums.page_titles import PageTitle

@allure.feature("Тесты авторизации")
class TestLogin:

    @allure.title("Позитивный тест авторизации")
    def test_positive_login(self, driver, login_page: LoginPage, product_page: ProductPage):
        login_page.login(UserFactory.admin())
        check.is_true(product_page.check_displaying_title(), "Заголовок не появился")
        check.equal(product_page.check_title(), PageTitle.PRODUCTS.value)

    @pytest.mark.parametrize("user, expected_error_message", [(UserFactory.unknown_user(), "Epic sadface: Username and password do not match any user in this service"), (UserFactory.locked(), "Epic sadface: Sorry, this user has been locked out."), (UserFactory.with_empty_username(), "Epic sadface: Username is required"), (UserFactory.with_empty_password(), "Epic sadface: Password is required")])
    @allure.title("Негативный тест авторизации")
    def test_negative_login(self, driver, user, expected_error_message, login_page: LoginPage):
        login_page.login(user)
        check.is_true(login_page.check_error_displaying(), "Ошибка не появилась")
        check.equal(login_page.check_error_text(), expected_error_message)