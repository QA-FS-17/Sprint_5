from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators, RecoveryPageLocators
from utils.generate_data import generate_email, generate_password


class TestLoginViaMainPage:
    """Тесты входа через кнопку на главной странице"""

    def test_successful_login(self, driver, register_user):
        """
        Проверка успешного входа через кнопку 'Войти в аккаунт' на главной
        """
        # Переход на главную страницу
        driver.get("https://stellarburgers.nomoreparties.site")

        # Клик по кнопке входа
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

        # Заполнение формы входа
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(register_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(register_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # Проверка успешного входа
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )
        assert "https://stellarburgers.nomoreparties.site/" in driver.current_url


class TestLoginViaPersonalAccount:
    """Тесты входа через кнопку 'Личный кабинет'"""

    def test_successful_login(self, driver, register_user):
        """
        Проверка успешного входа через кнопку в личном кабинете
        """
        # Переход на главную страницу
        driver.get("https://stellarburgers.nomoreparties.site")

        # Клик по кнопке личного кабинета
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Заполнение формы входа
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(register_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(register_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # Проверка успешного входа
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )


class TestLoginViaRecoveryForm:
    """Тесты входа через форму восстановления пароля"""

    def test_successful_login(self, driver, register_user):
        """
        Проверка успешного входа через ссылку в форме восстановления пароля
        """
        # Переход на страницу восстановления пароля
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        # Клик по ссылке "Войти"
        driver.find_element(*RecoveryPageLocators.LOGIN_LINK).click()

        # Заполнение формы входа
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(register_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(register_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # Проверка успешного входа
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )