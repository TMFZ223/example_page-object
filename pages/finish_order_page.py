import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FinishOrderPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.finish_button = (By.XPATH, "//button[@name ='finish']")

    def click_finish_button(self):
        self.driver.find_element(*self.finish_button).click()