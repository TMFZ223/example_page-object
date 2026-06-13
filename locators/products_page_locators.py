from selenium.webdriver.common.by import By

from locators.base_locators import BaseLocators
from locators.patterns import DATA_TEST_PATTERN

class ProductPageLocators(BaseLocators):
    cart_link = (By.CSS_SELECTOR, DATA_TEST_PATTERN.format("shopping-cart-link"))
    cart_counter = (By.CSS_SELECTOR, DATA_TEST_PATTERN.format("shopping-cart-badge"))
    ADD_TO_CART_PATTERN = "//*[text()='{}']//ancestor::div[@class='inventory_item']//child::button[text()='Add to cart']"
    REMOVE_PATTERN = "//*[text()='{}']//ancestor::div[@class='inventory_item']//child::button[text()='Remove']"