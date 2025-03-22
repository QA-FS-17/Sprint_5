from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_successful_registration(driver, register_user):
    # Ожидаем перенаправления на страницу логина
    WebDriverWait(driver, 5).until(
        EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
    )
    # Проверяем, что регистрация прошла успешно
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login", "Регистрация не удалась"