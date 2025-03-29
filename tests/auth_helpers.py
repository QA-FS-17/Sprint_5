from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import (LoginPageLocators, MainPageLocators)
from config import (LOGIN_URL, MAIN_PAGE_URL, DEFAULT_WAIT_TIME)


# Хелпер-класс для авторизации
class AuthHelper:
    @staticmethod
    def login(driver, email, password):
        driver.get(LOGIN_URL)
        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(email)

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(LoginPageLocators.PASSWORD_INPUT)
        ).send_keys(password)

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        ).click()

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.url_to_be(MAIN_PAGE_URL)
        )

    @staticmethod
    def assert_logged_in(driver):
        assert driver.current_url == MAIN_PAGE_URL
        assert WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()

    @staticmethod
    def assert_logged_out(driver):
        assert driver.current_url == LOGIN_URL
        assert WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        ).is_displayed()