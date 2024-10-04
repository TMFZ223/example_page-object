from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class AuthorizationPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.username_input = (By.XPATH, "//input[@placeholder='Username']")
        self.password_input = (By.XPATH, "//input[@placeholder='Password']")
        self.login_button = (By.XPATH, "//input[@value='Login']")

    def enter_username(self, username: str):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password: str):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()