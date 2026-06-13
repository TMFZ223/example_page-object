from utils.env_reader import EnvReader

base_url = EnvReader.get_env_variable_value("SAUCEDEMO_URL")
products_list = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]