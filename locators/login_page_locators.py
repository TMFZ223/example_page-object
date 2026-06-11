from selenium.webdriver.common.by import By

from locators.base_locators import DATA_TEST_PATTERN


class LoginPageLocators:
    username_input = (By.CSS_SELECTOR, DATA_TEST_PATTERN.format("username"))
    password_input = (By.CSS_SELECTOR, DATA_TEST_PATTERN.format("password"))
    login_button = (By.CSS_SELECTOR, "#login-button")
    error = (By.CSS_SELECTOR, DATA_TEST_PATTERN.format("error"))
