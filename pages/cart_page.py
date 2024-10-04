import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.cart_link = (By.XPATH, "//a[@class ='shopping_cart_link']")
    def go_cart(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.cart_link))
        self.driver.find_element(*self.cart_link).click()