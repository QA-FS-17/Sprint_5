from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators
from utils.generate_data import generate_email


class TestRegistration:
    """Тест регистрации пользователя"""

    def test_successful_registration(self, driver, register_user):
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
        )
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_invalid_password_registration(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys("Иван Иванов")
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("123")
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.ERROR_MESSAGE)
        )
        assert error.is_displayed()