from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_via_main_page_button(driver, register_user):

    # Шаг 1: Регистрация пользователя (фикстура register_user)
    # register_user зарегистрировала пользователя и вернула его данные (email и пароль)

    # Шаг 2: Открываем главную страницу
    driver.get("https://stellarburgers.nomoreparties.site")

    # Шаг 3: Нажимаем кнопку «Войти в аккаунт»
    login_button = driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']")
    login_button.click()

    # Шаг 4: Заполняем форму входа
    email = register_user["email"]
    password = register_user["password"]
    driver.find_element(By.XPATH, "//input[@name='name']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)

    # Шаг 5: Нажимаем кнопку «Войти»
    submit_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
    submit_button.click()

    # Шаг 6: Ожидаем перенаправления на главную страницу
    WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/")
    )

    # Шаг 7: Проверяем, что вход выполнен успешно
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/", "Вход не выполнен"