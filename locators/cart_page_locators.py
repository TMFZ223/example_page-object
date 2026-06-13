from selenium.webdriver.common.by import By

from locators.base_locators import BaseLocators
from locators.patterns import DATA_TEST_PATTERN

class CartPageLocators(BaseLocators):
    cart_product = (By.CSS_SELECTOR, ".inventory_item_name")
    continue_shopping = (By.CSS_SELECTOR, DATA_TEST_PATTERN.format("continue-shopping"))