from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.generate_data import generate_email, generate_password

def test_login_via_password_recovery(driver):
    # Загружаем страницу регистрации
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Регистрируем нового пользователя
    # Ввод имени
    name_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@name='name']"))
    )
    name_input.send_keys("Иван Иванов")

    # Ввод email
    email = generate_email()
    email_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[text()='Email']/following-sibling::input"))
    )
    email_input.send_keys(email)

    # Ввод пароля
    password = generate_password()
    password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[text()='Пароль']/following-sibling::input"))
    )
    password_input.send_keys(password)

    # Нажимаем кнопку "Зарегистрироваться"
    register_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Зарегистрироваться']"))
    )
    register_button.click()

    # Переход на страницу входа
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )

    # Вводим email и пароль на странице входа
    # Ввод email
    email_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@name='name']"))
    )
    email_input.send_keys(email)

    # Ввод пароля
    password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@name='Пароль']"))
    )
    password_input.send_keys(password)

    # Нажимаем кнопку "Войти"
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']"))
    )
    submit_button.click()

    # Переход на главную страницу
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    )

    # Переход в личный кабинет
    personal_account_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and contains(text(), 'Личный Кабинет')]"))
    )
    personal_account_button.click()

    # Нажимаем кнопку "Выйти"
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'Account_button__14Yp3') and contains(text(), 'Выход')]"))
    )
    logout_button.click()

    # Переход на страницу входа
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )

    # Нажимаем кнопку "Восстановить пароль"
    recovery_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Восстановить пароль']"))
    )
    recovery_button.click()

    # Переход на страницу восстановления пароля
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/forgot-password")
    )

    # Нажимаем кнопку "Войти" на странице восстановления пароля
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Войти']"))
    )
    login_button.click()

    # Переход на страницу входа
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )

    # Вводим email и пароль на странице входа
    # Ввод email
    email_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@name='name']"))
    )
    email_input.send_keys(email)

    # Ввод пароля
    password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@name='Пароль']"))
    )
    password_input.send_keys(password)

    # Нажимаем кнопку "Войти"
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']"))
    )
    submit_button.click()

    # Проверяем, что мы на главной странице
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    )

    # Проверяем URL главной страницы
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/", "Вход не выполнен"