import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.generate_data import generate_email, generate_password
from locators import (RegistrationPageLocators,
                      LoginPageLocators,
                      MainPageLocators,
                      PasswordRecoveryPageLocators,
                      PersonalAccountLocators)


# Тест на вход по кнопке «Войти в аккаунт» на главной странице
def test_registration_and_login(driver):
    # Загружаем страницу регистрации
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Регистрируем нового пользователя
    # Ввод имени
    name_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(RegistrationPageLocators.NAME_INPUT)
    )
    name_input.send_keys("Иван Иванов")

    # Ввод email
    email = generate_email()
    email_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(RegistrationPageLocators.EMAIL_INPUT)
    )
    email_input.send_keys(email)

    # Ввод пароля
    password = generate_password()
    password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(RegistrationPageLocators.PASSWORD_INPUT)
    )
    password_input.send_keys(password)

    # Нажимаем кнопку "Зарегистрироваться"
    register_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(RegistrationPageLocators.REGISTER_BUTTON)
    )
    register_button.click()

    # Ожидаем перехода на страницу входа
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )

    # Вход с только что созданными учетными данными
    # Ввод email
    email_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.EMAIL_INPUT)
    )
    email_input.send_keys(email)

    # Ввод пароля
    password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.PASSWORD_INPUT)
    )
    password_input.send_keys(password)

    # Нажимаем кнопку "Войти"
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
    )
    submit_button.click()

    # Проверяем, что мы на главной странице (убеждаемся, что вход выполнен)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
    )

    # Дополнительная проверка URL главной страницы
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/", "Вход не выполнен, URL не соответствует главной странице"


# Тест на вход через кнопку «Личный кабинет»
def test_login_via_personal_account(driver, register_user):
    # Получаем данные пользователя из фикстуры
    email = register_user["email"]
    password = register_user["password"]

    # Переход на страницу входа и авторизация
    driver.get("https://stellarburgers.nomoreparties.site/login")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.EMAIL_INPUT)
    ).send_keys(email)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.PASSWORD_INPUT)
    ).send_keys(password)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
    ).click()

    # Проверка успешного входа
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    )

    # Переход в личный кабинет и выход
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(PersonalAccountLocators.LOGOUT_BUTTON)
    ).click()

    # Проверка выхода
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )

    # Повторная авторизация
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.EMAIL_INPUT)
    ).send_keys(email)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.PASSWORD_INPUT)
    ).send_keys(password)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
    ).click()

    # Проверка входа
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    )

    # Переход в ЛК и возврат в конструктор
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(PersonalAccountLocators.CONSTRUCTOR_BUTTON)
    ).click()

    # Финальная проверка
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/", \
        "После всех действий не вернулись на главную страницу"


# Тест на вход через кнопку в форме регистрации
@pytest.mark.usefixtures("driver")
def test_login_via_registration_form_button(driver):
    # Регистрация нового пользователя
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Заполнение формы регистрации
    name_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(RegistrationPageLocators.NAME_INPUT)
    )
    name_input.send_keys("Иван Иванов")

    email = generate_email()
    email_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(RegistrationPageLocators.EMAIL_INPUT)
    )
    email_input.send_keys(email)

    password = generate_password()
    password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(RegistrationPageLocators.PASSWORD_INPUT)
    )
    password_input.send_keys(password)

    register_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(RegistrationPageLocators.REGISTER_BUTTON)
    )
    register_button.click()

    # Переход на страницу входа
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )

    # Вход в систему
    email_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.EMAIL_INPUT)
    )
    email_input.send_keys(email)

    password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.PASSWORD_INPUT)
    )
    password_input.send_keys(password)

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
    )
    submit_button.click()

    # Проверка успешного входа
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    )

    # Проверка, что мы на главной странице
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/", "Вход не выполнен"


# Тест на вход через кнопку в форме восстановления пароля
def test_login_via_password_recovery(driver):

    # Загружаем страницу регистрации
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Заполнение формы регистрации
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(RegistrationPageLocators.NAME_INPUT)
    ).send_keys("Иван Иванов")

    email = generate_email()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(RegistrationPageLocators.EMAIL_INPUT)
    ).send_keys(email)

    password = generate_password()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(RegistrationPageLocators.PASSWORD_INPUT)
    ).send_keys(password)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(RegistrationPageLocators.REGISTER_BUTTON)
    ).click()

    # Ожидание перехода на страницу входа
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )

    # Первичная авторизация
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.EMAIL_INPUT)
    ).send_keys(email)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.PASSWORD_INPUT)
    ).send_keys(password)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
    ).click()

    # Проверка успешного входа
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    )

    # Выход из аккаунта
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(PersonalAccountLocators.LOGOUT_BUTTON)
    ).click()

    # Ожидание перехода на страницу входа
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )

    # Переход на страницу восстановления пароля
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(PasswordRecoveryPageLocators.RECOVERY_LINK)
    ).click()

    # Проверка перехода на страницу восстановления
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/forgot-password")
    )

    # Возврат на страницу входа
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(PasswordRecoveryPageLocators.LOGIN_LINK)
    ).click()

    # Проверка перехода на страницу входа
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )

    # Повторная авторизация
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.EMAIL_INPUT)
    ).send_keys(email)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.PASSWORD_INPUT)
    ).send_keys(password)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
    ).click()

    # Проверка успешного входа
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    )

    # Проверка URL главной страницы
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/", \
        "Ошибка: вход не выполнен, URL не соответствует главной странице"