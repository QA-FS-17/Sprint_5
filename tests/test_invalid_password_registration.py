from selenium.webdriver.common.by import By
from utils.generate_data import generate_email

def test_invalid_password_registration(driver):
    # Открываем страницу регистрации
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Заполняем форму регистрации с некорректным паролем
    driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Иван Иванов")
    driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(generate_email())
    driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input").send_keys("123")

    # Нажимаем кнопку "Зарегистрироваться"
    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

    # Проверяем, что отображается ошибка
    error_message = driver.find_element(By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")
    assert error_message.is_displayed(), "Ошибка для некорректного пароля не отображается"