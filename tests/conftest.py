import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators, MainPageLocators, PersonalAccountLocators
from config import REGISTER_URL, LOGIN_URL, DEFAULT_WAIT_TIME
from auth_helpers import AuthHelper
from utils.generate_data import generate_email, generate_password


# Фикстуры
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
        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(RegistrationPageLocators.NAME_INPUT)
        ).send_keys("Test User")

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(RegistrationPageLocators.EMAIL_INPUT)
        ).send_keys(random_user["email"])

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(RegistrationPageLocators.PASSWORD_INPUT)
        ).send_keys(random_user["password"])

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(RegistrationPageLocators.REGISTER_BUTTON)
        ).click()

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.url_to_be(LOGIN_URL)
        )
        return random_user

    return _register


@pytest.fixture
def login_user(driver, register_user):
    def _login():
        user = register_user()
        AuthHelper.login(driver, user["email"], user["password"])
        return user

    return _login


@pytest.fixture
def logout_user(driver):
    def _logout():
        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(PersonalAccountLocators.LOGOUT_BUTTON)
        ).click()

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.url_to_be(LOGIN_URL)
        )

    return _logout
