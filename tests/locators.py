# Локаторы
class LoginPageLocators:
    class MainPageLocators:
        ORDER_BUTTON = ("xpath", "//button[contains(text(),'Order')]")
        PERSONAL_ACCOUNT_BUTTON = ("xpath", "//a[@href='/account']")
        LOGIN_BUTTON = ("xpath", "//button[contains(text(),'Войти в аккаунт')]")

class RegistrationPageLocators:
    NAME_INPUT = ("id", "name")
    EMAIL_INPUT = ("id", "email")
    PASSWORD_INPUT = ("id", "password")
    REGISTER_BUTTON = ("xpath", "//button[@type='submit']")
    LOGIN_LINK = ("link text", "Already have an account?")

class MainPageLocators:
    ORDER_BUTTON = ("xpath", "//button[contains(text(),'Order')]")
    PERSONAL_ACCOUNT_BUTTON = ("xpath", "//a[@href='/account']")

class PersonalAccountLocators:
    LOGOUT_BUTTON = ("xpath", "//button[contains(text(),'Logout')]")
