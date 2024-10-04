from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.product = (By.XPATH, "//img[@alt ='Sauce Labs Backpack']")
        self.cart_button = (By.XPATH, "//button[@name ='add-to-cart']")

    def choose_product(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.product))
        self.driver.find_element(*self.product).click()
    def add_product_to_cart(self):

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.cart_button))
        self.driver.find_element(*self.cart_button).click()