import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.generate_data import generate_email, generate_password


@pytest.fixture
def driver():
    """Фикстура инициализации драйвера"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def register_user(driver):
    """Фикстура регистрации нового пользователя"""
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Заполнение формы регистрации
    driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Иван Иванов")
    email = generate_email()
    driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(email)
    password = generate_password()
    driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

    # Ожидание успешной регистрации
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )

    return {"email": email, "password": password}


@pytest.fixture
def login_user(driver, register_user):
    """Фикстура авторизации пользователя"""
    # Используем данные из register_user
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(By.XPATH, "//input[@name='name']").send_keys(register_user["email"])
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(register_user["password"])
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    # Ожидание успешного входа
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]"))
    )

    return register_user  # Возвращаем те же данные


@pytest.fixture
def logout_user(driver, login_user):
    """Фикстура выхода из системы"""
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").click()

    # Ожидание загрузки ЛК
    WebDriverWait(driver, 10).until(
        EC.url_contains("/account/profile")
    )

    # Выход
    driver.find_element(By.XPATH, "//button[contains(text(), 'Выход')]").click()

    # Ожидание выхода
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )

    return login_user  # Возвращаем данные пользователя