from selenium.webdriver.common.by import By
from locators.patterns import DATA_TEST_PATTERN

class BaseLocators:
    page_title = (By.CSS_SELECTOR, DATA_TEST_PATTERN.format("title"))