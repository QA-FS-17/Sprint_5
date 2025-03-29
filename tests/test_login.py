from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators, LoginPageLocators, MainPageLocators, ForgotPasswordPageLocators
from utils.generate_data import generate_email, generate_password

BASE_URL = "https://stellarburgers.nomoreparties.site"


class TestLoginFromRegistration:
    def test_successful_login_after_registration(self, driver):
        """Тест успешного входа после регистрации"""
        # 1. Открываем страницу регистрации
        driver.get(f"{BASE_URL}/register")

        # Генерируем тестовые данные
        test_email = generate_email()
        test_password = generate_password(8)  # Генерируем пароль из 8 символов

        # 2. Регистрируемся
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)
        ).send_keys("Test User")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_INPUT)
        ).send_keys(test_email)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.PASSWORD_INPUT)
        ).send_keys(test_password)

        # 3. Нажимаем кнопку "Зарегистрироваться"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.REGISTER_BUTTON)
        ).click()

        # 4. Проверяем, что открылась страница логирования
        WebDriverWait(driver, 10).until(
            EC.url_to_be(f"{BASE_URL}/login")
        )

        # 5. Вводим зарегистрированные данные
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(test_email)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.PASSWORD_INPUT)
        ).send_keys(test_password)

        # 6. Нажимаем кнопку "Войти"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        ).click()

        # 7. Проверяем, что мы на главной странице
        WebDriverWait(driver, 10).until(
            EC.url_to_be(f"{BASE_URL}/")
        )
        assert driver.current_url == f"{BASE_URL}/"


class TestLoginFromPersonalAccountButton:
    def test_login_via_personal_account_button(self, driver, register_user):
        """Тест входа через кнопку 'Личный кабинет'"""
        user = register_user()
        driver.get(BASE_URL)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(user["email"])

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.PASSWORD_INPUT)
        ).send_keys(user["password"])

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be(f"{BASE_URL}/")
        )
        assert driver.current_url == f"{BASE_URL}/"

class TestLoginFromRegistrationPage:
    def test_login_via_registration_page_button(self, driver, register_user):
        """Тест входа через кнопку в форме регистрации"""
        user = register_user()
        driver.get(f"{BASE_URL}/register")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_LINK)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(user["email"])

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.PASSWORD_INPUT)
        ).send_keys(user["password"])

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be(f"{BASE_URL}/")
        )
        assert driver.current_url == f"{BASE_URL}/"

class TestLoginFromForgotPasswordPage:
    def test_login_via_forgot_password_page_button(self, driver, register_user):
        """Тест входа через кнопку в форме восстановления пароля"""
        user = register_user()
        driver.get(f"{BASE_URL}/forgot-password")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ForgotPasswordPageLocators.LOGIN_LINK)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(user["email"])

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.PASSWORD_INPUT)
        ).send_keys(user["password"])

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be(f"{BASE_URL}/")
        )
        assert driver.current_url == f"{BASE_URL}/"