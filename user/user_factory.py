from user.user import User
from utils.env_reader import EnvReader

class UserFactory:

    @staticmethod
    def admin():
        return User(username=EnvReader.get_env_variable_value("SAUCEDEMO_ADMIN_USER"), password=EnvReader.get_env_variable_value("SAUCEDEMO_ADMIN_PASSWORD"))

    @staticmethod
    def unknown_user():
        return User(username=EnvReader.get_env_variable_value("SAUCEDEMO_WRONG_USER"), password=EnvReader.get_env_variable_value("SAUCEDEMO_ADMIN_PASSWORD"))

    @staticmethod
    def locked():
        return User(username=EnvReader.get_env_variable_value("SAUCEDEMO_LOCKED_USER"), password=EnvReader.get_env_variable_value("SAUCEDEMO_ADMIN_PASSWORD"))

    @staticmethod
    def with_empty_username():
        return User(username="", password=EnvReader.get_env_variable_value("SAUCEDEMO_ADMIN_PASSWORD"))

    @staticmethod
    def with_empty_password():
        return User(username=EnvReader.get_env_variable_value("SAUCEDEMO_ADMIN_USER"), password="")