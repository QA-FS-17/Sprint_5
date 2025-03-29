import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators, LoginPageLocators
from utils.generate_data import generate_email, generate_password

BASE_URL = "https://stellarburgers.nomoreparties.site"
REGISTER_URL = f"{BASE_URL}/register"
LOGIN_URL = f"{BASE_URL}/login"
DEFAULT_WAIT_TIME = 10


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def random_user():
    return {"email": generate_email(), "password": generate_password()}


@pytest.fixture
def register_user(driver, random_user):
    def _register():
        driver.get(REGISTER_URL)

        try:
            # Заполнение формы регистрации
            WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
                EC.presence_of_element_located(RegistrationPageLocators.NAME_INPUT)
            ).send_keys("Test User")

            WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
                EC.presence_of_element_located(RegistrationPageLocators.EMAIL_INPUT)
            ).send_keys(random_user["email"])

            WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
                EC.presence_of_element_located(RegistrationPageLocators.PASSWORD_INPUT)
            ).send_keys(random_user["password"])

            # Нажатие кнопки регистрации
            WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
                EC.element_to_be_clickable(RegistrationPageLocators.REGISTER_BUTTON)
            ).click()

            # Ожидание перехода на страницу входа
            WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
                EC.url_to_be(LOGIN_URL)
            )
            return random_user
        except Exception as e:
            print(f"Error during registration: {e}")
            driver.save_screenshot("registration_error.png")
            raise

    return _register


@pytest.fixture
def login_user(driver, register_user):
    def _login():
        user = register_user()
        # Вход в систему
        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(user["email"])

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.presence_of_element_located(LoginPageLocators.PASSWORD_INPUT)
        ).send_keys(user["password"])

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        ).click()

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.url_to_be(f"{BASE_URL}/")
        )
        return user

    return _login