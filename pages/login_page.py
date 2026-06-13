import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from user.user import User


class LoginPage(BasePage):
    locators = LoginPageLocators()


    @allure.step("Заполнить форму логина")
    def login(self, user: User):
        self.enter_username(user.username)
        self.enter_password(user.password)
        self.click_login_button()

    @allure.step("Ввести в поле username значение {username}")
    def enter_username(self, username: str):
        self.element_is_visible(self.locators.username_input).send_keys(username)

    @allure.step("Ввести в поле password значение {password}")
    def enter_password(self, password: str):
        self.element_is_visible(self.locators.password_input).send_keys(password)

    @allure.step("Нажать на кнопку входа")
    def click_login_button(self):
        self.element_is_visible(self.locators.login_button).click()

    @allure.step("Проверить наличие ошибки входа на страницы")
    def check_error_displaying(self):
        return self.element_is_visible(self.locators.error).is_displayed()

    @allure.step("Проверить текст ошибки входа")
    def check_error_text(self):
        return self.element_is_visible(self.locators.error).text