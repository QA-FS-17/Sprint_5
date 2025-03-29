from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators


BASE_URL = "https://stellarburgers.nomoreparties.site"
DEFAULT_WAIT_TIME = 10

class TestSuccessfulRegistration:
    """Тесты успешной регистрации"""

    def test_successful_registration(self, driver, register_user):
        """Проверка успешной регистрации"""
        register_user()  # Фикстура уже содержит все шаги регистрации

        # Проверяем переход на страницу логина
        WebDriverWait(driver, 10).until(
            EC.url_to_be(f"{BASE_URL}/login")
        )
        assert driver.current_url == f"{BASE_URL}/login"


class TestRegistrationErrors:
    """Тесты ошибок при регистрации"""

    def test_weak_password_error(self, driver, weak_password_user):
        """Проверка ошибки 'Некорректный пароль'"""
        driver.get(f"{BASE_URL}/register")

        # Заполняем форму со слабым паролем
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)
        ).send_keys(weak_password_user["name"])

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_INPUT)
        ).send_keys(weak_password_user["email"])

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.PASSWORD_INPUT)
        ).send_keys(weak_password_user["password"])

        # Проверяем сообщение об ошибке
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.REGISTER_BUTTON)
        ).click()

        error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.PASSWORD_ERROR)
        )
        assert error.text == "Некорректный пароль"