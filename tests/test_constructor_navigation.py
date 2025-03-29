from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from conftest import BASE_URL, DEFAULT_WAIT_TIME
from locators import ConstructorPageLocators


class TestConstructorNavigation:
    def test_buns_tab_active_by_default(self, driver):
        """Проверить, что таб 'Булки' активен при загрузке страницы"""
        driver.get(BASE_URL)

        # Проверяем, что таб "Булки" активен
        active_tab = WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB)
        )
        buns_text = active_tab.find_element(*ConstructorPageLocators.BUNS_TEXT)
        assert buns_text.is_displayed(), "По умолчанию должен быть активен таб 'Булки'"

    def test_switch_to_sauces_section(self, driver):
        """Проверить переключение на таб 'Соусы'"""
        driver.get(BASE_URL)

        # Кликаем на таб "Соусы"
        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(ConstructorPageLocators.SAUCES_TAB)
        ).click()

        # Проверяем, что таб "Соусы" стал активным
        active_tab = WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB)
        )
        sauces_text = active_tab.find_element(*ConstructorPageLocators.SAUCES_TEXT)
        assert sauces_text.is_displayed(), "После клика должен быть активен таб 'Соусы'"

    def test_switch_to_fillings_section(self, driver):
        """Проверить переключение на таб 'Начинки'"""
        driver.get(BASE_URL)

        # Кликаем на таб "Начинки"
        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(ConstructorPageLocators.FILLINGS_TAB)
        ).click()

        # Проверяем, что таб "Начинки" стал активным
        active_tab = WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB)
        )
        fillings_text = active_tab.find_element(*ConstructorPageLocators.FILLINGS_TEXT)
        assert fillings_text.is_displayed(), "После клика должен быть активен таб 'Начинки'"

    def test_switch_back_to_buns_section(self, driver):
        """Проверить возврат к табу 'Булки' после переключения"""
        driver.get(BASE_URL)

        # 1. Проверяем начальное состояние
        active_tab = WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB)
        )
        assert active_tab.find_element(*ConstructorPageLocators.BUNS_TEXT).is_displayed(), \
            "Изначально должен быть активен таб 'Булки'"

        # 2. Переключаемся на "Соусы"
        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(ConstructorPageLocators.SAUCES_TAB)
        ).click()

        # 3. Проверяем активность "Соусов"
        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            lambda d: d.find_element(
                *ConstructorPageLocators.ACTIVE_TAB
            ).find_element(
                *ConstructorPageLocators.SAUCES_TEXT
            ).is_displayed()
        )

        # 4. Возвращаемся к "Булкам"
        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(ConstructorPageLocators.BUNS_TAB)
        ).click()

        # 5. Проверяем активность "Булок"
        WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            lambda d: d.find_element(
                *ConstructorPageLocators.ACTIVE_TAB
            ).find_element(
                *ConstructorPageLocators.BUNS_TEXT
            ).is_displayed()
        )