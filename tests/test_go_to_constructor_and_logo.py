from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_navigation_via_buttons(driver):
    # Загружаем страницу регистрации
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Нажимаем на кнопку "Конструктор"
    constructor_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Конструктор')]"))
    )
    constructor_button.click()

    # Проверяем, что мы на главной странице
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    )
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/", "Переход на главную страницу через кнопку 'Конструктор' не выполнен"

    # Нажимаем на кнопку "Войти в аккаунт"
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))
    )
    login_button.click()

    # Проверяем, что мы на странице входа
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login", "Переход на страницу входа не выполнен"

    # Нажимаем на логотип "Stellar Burgers"
    logo_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'AppHeader_header__logo__2D0X2')]"))
    )
    logo_button.click()

    # Проверяем, что мы на главной странице
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    )
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/", "Переход на главную страницу через логотип не выполнен"