import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from utils.env_reader import EnvReader
from pages.login_page import LoginPage
from pages.product_page import ProductPage
base_url = EnvReader.get_env_variable_value("SAUCEDEMO_URL")

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--guest")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    login_page = LoginPage(driver)
    login_page.open(base_url)
    return login_page

@pytest.fixture
def product_page(driver):
    return ProductPage(driver)