from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_logout_from_personal_account(driver, register_user):
    # Получаем email и пароль из фикстуры register_user
    email = register_user["email"]
    password = register_user["password"]

    # Регистрация (выполняется фикстурой register_user)

    # Переход на страницу входа
    driver.get("https://stellarburgers.nomoreparties.site/login")

    # Ввод данных для входа
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

    # Ожидаем перенаправления на главную страницу
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    )

    # Переход на страницу "Личный кабинет"
    personal_account_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and contains(text(), 'Личный Кабинет')]"))
    )
    personal_account_button.click()

    # Нажимаем кнопку "Выход"
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'Account_button__14Yp3') and contains(text(), 'Выход')]"))
    )
    logout_button.click()

    # Проверяем, что выход выполнен (перенаправление на страницу входа)
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login", "Выход из личного кабинета не выполнен"