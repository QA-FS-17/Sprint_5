from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators, PersonalAccountLocators, LoginPageLocators
from conftest import BASE_URL, DEFAULT_WAIT_TIME


class TestNavigation:
    def test_click_personal_account_button(self, driver, register_user):
        """Проверить переход по клику на «Личный кабинет»"""
        # Регистрируем пользователя
        user = register_user()

        # Логинимся
        driver.get(f"{BASE_URL}/login")
        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(user["email"])

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(LoginPageLocators.PASSWORD_INPUT)
        ).send_keys(user["password"])

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        ).click()

        # Переходим в личный кабинет
        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()

        # Проверяем, что мы на странице профиля
        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(PersonalAccountLocators.PROFILE_LINK)
        )

        assert driver.current_url == f"{BASE_URL}/account/profile"

    def test_click_constructor_button(self, driver, register_user):
        """Проверить переход по клику на «Конструктор»"""
        # Регистрируем и логинимся
        user = register_user()
        driver.get(f"{BASE_URL}/login")
        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(user["email"])

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(LoginPageLocators.PASSWORD_INPUT)
        ).send_keys(user["password"])

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        ).click()

        # Переходим в личный кабинет
        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()

        # Нажимаем на конструктор
        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(("css selector", "p.AppHeader_header__linkText__3q_va"))
        ).click()

        assert driver.current_url == f"{BASE_URL}/"

    def test_click_logo_button(self, driver, register_user):
        """Проверить переход по клику на логотип Stellar Burgers"""
        # Регистрируем и логинимся
        user = register_user()
        driver.get(f"{BASE_URL}/login")
        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(user["email"])

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(LoginPageLocators.PASSWORD_INPUT)
        ).send_keys(user["password"])

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        ).click()

        # Переходим в личный кабинет
        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()

        # Нажимаем на логотип
        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(("css selector", "div.AppHeader_header__logo__2D0X2"))
        ).click()

        assert driver.current_url == f"{BASE_URL}/"


class TestAccountNavigation:
    def test_logout_from_personal_account(self, driver, register_user):
        """
        Проверить выход по кнопке «Выйти» в личном кабинете
        """
        # 1. Регистрация и вход
        user = register_user()
        driver.get(f"{BASE_URL}/login")

        # Заполнение формы входа
        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        ).send_keys(user["email"])

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(LoginPageLocators.PASSWORD_INPUT)
        ).send_keys(user["password"])

        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        ).click()

        # 2. Переход в личный кабинет
        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        ).click()

        # 3. Выход из аккаунта
        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(PersonalAccountLocators.LOGOUT_BUTTON)
        ).click()

        # 4. Проверка перенаправления
        WebDriverWait(driver, DEFAULT_WAIT_TIME * 3).until(
            EC.url_to_be(f"{BASE_URL}/login")
        )
        assert driver.current_url == f"{BASE_URL}/login"
