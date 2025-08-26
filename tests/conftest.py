import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators
from utils.generate_data import generate_email, generate_password

BASE_URL = "https://stellarburgers.nomoreparties.site"
DEFAULT_WAIT_TIME = 10

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def random_user():
    return {
        "name": "Test User",
        "email": generate_email(),
        "password": generate_password(8)
    }

@pytest.fixture
def weak_password_user():
    return {
        "name": "Test User",
        "email": generate_email(),
        "password": "123"  # Специально слабый пароль
    }

@pytest.fixture
def register_user(driver, random_user):
    def _register():
        driver.get(f"{BASE_URL}/register")
        try:
            WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
                EC.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)
            ).send_keys(random_user["name"])

            WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
                EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_INPUT)
            ).send_keys(random_user["email"])

            WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
                EC.visibility_of_element_located(RegistrationPageLocators.PASSWORD_INPUT)
            ).send_keys(random_user["password"])

            WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
                EC.element_to_be_clickable(RegistrationPageLocators.REGISTER_BUTTON)
            ).click()

            return random_user
        except Exception as e:
            driver.save_screenshot("registration_error.png")
            pytest.fail(f"Ошибка регистрации: {str(e)}")

    return _register
