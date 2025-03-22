from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)

def test_login_via_personal_account(driver, register_user):
    # Получаем email и пароль из фикстуры register_user
    email = register_user["email"]
    password = register_user["password"]

    # Шаг 1: Регистрация (выполняется фикстурой register_user)

    # Шаг 2: Переход на страницу входа
    logging.info("Шаг 2: Переход на страницу входа")
    driver.get("https://stellarburgers.nomoreparties.site/login")

    # Шаг 3: Ввод данных для входа
    logging.info("Шаг 3: Ввод данных для входа")
    try:
        # Ввод email
        email_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='name']"))
        )
        email_input.send_keys(email)
        logging.info(f"Введен email: {email}")

        # Ввод пароля
        password_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='Пароль']"))
        )
        password_input.send_keys(password)
        logging.info(f"Введен пароль: {password}")
    except TimeoutException:
        logging.error("Поля ввода email или пароля не найдены или недоступны")
        driver.save_screenshot("input_fields_failed.png")
        raise

    # Шаг 4: Нажимаем кнопку "Войти"
    logging.info("Шаг 4: Нажимаем кнопку 'Войти'")
    try:
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']"))
        )
        submit_button.click()
        logging.info("Кнопка 'Войти' успешно нажата")
    except TimeoutException:
        logging.error("Кнопка 'Войти' не найдена или недоступна")
        driver.save_screenshot("login_button_failed.png")
        raise

    # Шаг 5: Ожидаем перенаправления на главную страницу
    logging.info("Шаг 5: Ожидаем перенаправления на главную страницу")
    try:
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )
        logging.info("Перенаправление на главную страницу успешно")
    except TimeoutException:
        logging.error("Перенаправление на главную страницу не произошло")
        driver.save_screenshot("redirect_failed.png")
        raise

    # Шаг 6: Переход на страницу "Личный кабинет"
    logging.info("Шаг 6: Переход на страницу 'Личный кабинет'")
    try:
        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and contains(text(), 'Личный Кабинет')]"))
        )
        personal_account_button.click()
        logging.info("Переход на страницу 'Личный кабинет' успешен")
    except TimeoutException:
        logging.error("Кнопка 'Личный кабинет' не найдена или недоступна")
        driver.save_screenshot("personal_account_button_failed.png")
        raise

    # Шаг 7: Нажимаем кнопку "Выход"
    logging.info("Шаг 7: Нажимаем кнопку 'Выход'")
    try:
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'Account_button__14Yp3') and contains(text(), 'Выход')]"))
        )
        logout_button.click()
        logging.info("Кнопка 'Выход' успешно нажата")
    except TimeoutException:
        logging.error("Кнопка 'Выход' не найдена или недоступна")
        driver.save_screenshot("logout_button_failed.png")
        raise

    # Шаг 8: Ожидаем перенаправления на страницу входа
    logging.info("Шаг 8: Ожидаем перенаправления на страницу входа")
    try:
        # Логируем текущий URL перед ожиданием
        logging.info(f"Текущий URL перед ожиданием: {driver.current_url}")

        # Ожидаем перенаправления на страницу входа
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
        )
        logging.info("Перенаправление на страницу входа успешно")
    except TimeoutException:
        # Логируем текущий URL при ошибке
        logging.error(f"Перенаправление на страницу входа не произошло. Текущий URL: {driver.current_url}")
        driver.save_screenshot("redirect_failed_after_logout.png")
        raise

    # Повтор шагов 3, 4, 5 для повторного входа
    logging.info("Повтор шагов 3, 4, 5 для повторного входа")

    # Шаг 3: Ввод данных для входа
    logging.info("Шаг 3: Ввод данных для входа")
    try:
        # Ввод email
        email_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='name']"))
        )
        email_input.send_keys(email)
        logging.info(f"Введен email: {email}")

        # Ввод пароля
        password_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='Пароль']"))
        )
        password_input.send_keys(password)
        logging.info(f"Введен пароль: {password}")
    except TimeoutException:
        logging.error("Поля ввода email или пароля не найдены или недоступны")
        driver.save_screenshot("input_fields_failed.png")
        raise

    # Шаг 4: Нажимаем кнопку "Войти"
    logging.info("Шаг 4: Нажимаем кнопку 'Войти'")
    try:
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']"))
        )
        submit_button.click()
        logging.info("Кнопка 'Войти' успешно нажата")
    except TimeoutException:
        logging.error("Кнопка 'Войти' не найдена или недоступна")
        driver.save_screenshot("login_button_failed.png")
        raise

    # Шаг 5: Ожидаем перенаправления на главную страницу
    logging.info("Шаг 5: Ожидаем перенаправления на главную страницу")
    try:
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/")
        )
        logging.info("Перенаправление на главную страницу успешно")
    except TimeoutException:
        logging.error("Перенаправление на главную страницу не произошло")
        driver.save_screenshot("redirect_failed.png")
        raise

    # Шаг 6: Переход на страницу "Личный кабинет"
    logging.info("Шаг 6: Переход на страницу 'Личный кабинет'")
    try:
        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and contains(text(), 'Личный Кабинет')]"))
        )
        personal_account_button.click()
        logging.info("Переход на страницу 'Личный кабинет' успешен")
    except TimeoutException:
        logging.error("Кнопка 'Личный кабинет' не найдена или недоступна")
        driver.save_screenshot("personal_account_button_failed.png")
        raise

    # Шаг 9: Переход из личного кабинета на главную страницу
    logging.info("Шаг 9: Переход из личного кабинета на главную страницу")
    try:
        # Нажимаем кнопку "Конструктор" для возврата на главную страницу
        constructor_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Конструктор')]"))
        )
        constructor_button.click()
        logging.info("Переход на главную страницу успешен")
    except TimeoutException:
        logging.error("Кнопка 'Конструктор' не найдена или недоступна")
        driver.save_screenshot("constructor_button_failed.png")
        raise

    # Проверяем, что мы на главной странице
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/", "Переход на главную страницу не выполнен"