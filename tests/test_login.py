import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import (LoginPageLocators, MainPageLocators,
                      RegistrationPageLocators, PersonalAccountLocators)
from config import (LOGIN_URL, MAIN_PAGE_URL,
                    REGISTER_URL, FORGOT_PASSWORD_URL,
                    DEFAULT_WAIT_TIME)
from auth_helpers import AuthHelper


class TestLoginFromMainPage:
    """Тесты входа через кнопку 'Войти в аккаунт' на главной странице"""

    def test_login_from_main_page_button(self, driver, login_user, logout_user):
        """Проверка входа через кнопку на главной странице"""
        logout_user()
        driver.get(MAIN_PAGE_URL)

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        ).click()

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.url_to_be(LOGIN_URL))

        user = login_user()
        AuthHelper.assert_logged_in(driver)
        assert driver.current_url == MAIN_PAGE_URL


class TestLoginFromPersonalAccountButton:
    """Тесты входа через кнопку 'Личный кабинет'"""

    def test_login_from_personal_account_button(self, driver, login_user, logout_user):
        """Проверка входа через кнопку личного кабинета"""
        logout_user()
        driver.get(MAIN_PAGE_URL)

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)  # Исправлена опечатка
        ).click()

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.url_to_be(LOGIN_URL))

        user = login_user()
        AuthHelper.assert_logged_in(driver)
        assert driver.current_url == MAIN_PAGE_URL


class TestLoginFromRegistrationForm:
    """Тесты входа через кнопку в форме регистрации"""

    def test_login_link_in_registration_form(self, driver, random_user):
        """Проверка перехода на страницу входа из формы регистрации"""
        driver.get(REGISTER_URL)

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_LINK)
        ).click()

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.url_to_be(LOGIN_URL))

        assert driver.current_url == LOGIN_URL
        assert WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        ).is_displayed()


class TestLoginFromPasswordRecoveryForm:
    """Тесты входа через кнопку в форме восстановления пароля"""

    def test_login_link_in_password_recovery_form(self, driver):
        """Проверка перехода на страницу входа из формы восстановления пароля"""
        driver.get(FORGOT_PASSWORD_URL)

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(LoginPageLocators.RECOVERY_LINK)
        ).click()

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.url_to_be(LOGIN_URL))

        assert driver.current_url == LOGIN_URL
        assert WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        ).is_displayed()