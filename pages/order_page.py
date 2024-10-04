from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.buy_button = (By.XPATH, "//button[@name ='checkout']")
        self.firstname_input = (By.XPATH, "//input[@placeholder='First Name']")
        self.lastname_input = (By.XPATH, "//input[@placeholder='Last Name']")
        self.zip_postal_cod_input = (By.XPATH, "//input[@placeholder='Zip/Postal Code']")
        self.next_button = (By.XPATH, "//input[@type ='submit']")

    def click_buy_button(self):
        self.driver.find_element(*self.buy_button).click()
    def enter_firstname(self, your_firstname: str):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.firstname_input))
        self.driver.find_element(*self.firstname_input).send_keys(your_firstname)

    def enter_lastname(self, your_lastname: str):
        self.driver.find_element(*self.lastname_input).send_keys(your_lastname)
    def enter_zip_postal_cod(self, your_zip_postal_cod: str):
        self.driver.find_element(*self.zip_postal_cod_input).send_keys(your_zip_postal_cod)
    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()