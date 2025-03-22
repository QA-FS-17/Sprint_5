import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.generate_data import generate_email, generate_password

# Фикстура для инициализации драйвера
@pytest.fixture
def driver():
    # Настройка драйвера для Chrome
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Фикстура для регистрации пользователя
@pytest.fixture
def register_user(driver):
    # Открываем страницу регистрации
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Заполняем форму регистрации
    driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Иван Иванов")
    email = generate_email()
    driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(email)
    password = generate_password()
    driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input").send_keys(password)

    # Нажимаем кнопку "Зарегистрироваться"
    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

    # Возвращаем email и пароль для использования в тестах
    return {"email": email, "password": password}

# Фикстура для входа пользователя
@pytest.fixture
def login_user(driver, register_user):
    # Получаем email и пароль из фикстуры register_user
    email = register_user["email"]
    password = register_user["password"]

    # Открываем страницу входа
    driver.get("https://stellarburgers.nomoreparties.site/login")

    # Заполняем форму входа
    driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(email)
    driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input").send_keys(password)

    # Нажимаем кнопку "Войти"
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    # Ожидаем перенаправления на главную страницу
    WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    )

    # Возвращаем email и пароль для использования в тестах
    return {"email": email, "password": password}

# Фикстура для выхода пользователя
@pytest.fixture
def logout_user(driver):
    # Открываем главную страницу
    driver.get("https://stellarburgers.nomoreparties.site")

    # Нажимаем кнопку "Личный кабинет"
    personal_account_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and contains(text(), 'Личный Кабинет')]"))
    )
    personal_account_button.click()

    # Ожидаем появления кнопки "Выход"
    try:
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'Account_button__14Yp3') and contains(text(), 'Выход')]"))
        )
        logout_button.click()
    except TimeoutException:
        # Если кнопка "Выход" не найдена, делаем скриншот для отладки
        driver.save_screenshot("logout_error.png")
        raise

    # Ожидаем перенаправления на главную страницу
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    )