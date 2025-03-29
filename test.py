from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from conftest import BASE_URL, DEFAULT_WAIT_TIME
from locators import ConstructorPageLocators


class TestConstructorNavigation:
    def highlight_element(self, driver, element, duration=1):
        """Подсвечиваем элемент на время выполнения теста"""
        original_style = element.get_attribute("style")
        driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element,
            "border: 3px solid red; background: yellow;"
        )
        sleep(duration)
        driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element,
            original_style
        )

    def test_buns_tab_active_by_default(self, driver):
        """Проверить, что таб 'Булки' активен при загрузке страницы"""
        driver.get(BASE_URL)
        sleep(1)  # Пауза для визуальной проверки

        active_tab = WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB)
        )
        self.highlight_element(driver, active_tab)

        buns_text = active_tab.find_element(*ConstructorPageLocators.BUNS_TEXT)
        assert buns_text.is_displayed(), "По умолчанию должен быть активен таб 'Булки'"

    def test_switch_to_sauces_section(self, driver):
        """Проверить переключение на таб 'Соусы'"""
        driver.get(BASE_URL)
        sleep(1)

        # Подсвечиваем таб "Булки" перед переключением
        buns_tab = driver.find_element(*ConstructorPageLocators.BUNS_TAB)
        self.highlight_element(driver, buns_tab)

        # Кликаем на таб "Соусы" с визуальным подтверждением
        sauces_tab = WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(ConstructorPageLocators.SAUCES_TAB)
        )
        self.highlight_element(driver, sauces_tab, 2)
        sauces_tab.click()
        sleep(1)  # Пауза для визуализации переключения

        # Проверяем активность "Соусов"
        active_tab = WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB)
        )
        self.highlight_element(driver, active_tab, 3)

        sauces_text = active_tab.find_element(*ConstructorPageLocators.SAUCES_TEXT)
        assert sauces_text.is_displayed(), "После клика должен быть активен таб 'Соусы'"

    def test_switch_to_fillings_section(self, driver):
        """Проверить переключение на таб 'Начинки'"""
        driver.get(BASE_URL)
        sleep(1)

        fillings_tab = WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(ConstructorPageLocators.FILLINGS_TAB)
        )

        # Добавляем анимацию наведения
        ActionChains(driver).move_to_element(fillings_tab).pause(1).perform()
        self.highlight_element(driver, fillings_tab, 2)
        fillings_tab.click()
        sleep(1)

        active_tab = WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB)
        )
        self.highlight_element(driver, active_tab, 3)

        fillings_text = active_tab.find_element(*ConstructorPageLocators.FILLINGS_TEXT)
        assert fillings_text.is_displayed(), "После клика должен быть активен таб 'Начинки'"

    def test_switch_back_to_buns_section(self, driver):
        """Проверить возврат к табу 'Булки' после переключения"""
        driver.get(BASE_URL)
        sleep(1)

        # 1. Проверяем начальное состояние
        active_tab = WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB)
        )
        self.highlight_element(driver, active_tab, 2)

        # 2. Переключаемся на "Соусы" с визуализацией
        sauces_tab = WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(ConstructorPageLocators.SAUCES_TAB)
        )
        ActionChains(driver).move_to_element(sauces_tab).pause(1).click().perform()
        sleep(1)

        # 3. Проверяем активность "Соусов"
        active_tab = WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB)
        )
        self.highlight_element(driver, active_tab, 2)

        # 4. Возвращаемся к "Булкам" с визуализацией
        buns_tab = WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(ConstructorPageLocators.BUNS_TAB)
        )
        ActionChains(driver).move_to_element(buns_tab).pause(1).click().perform()
        sleep(1)

        # 5. Проверяем активность "Булок"
        active_tab = WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(ConstructorPageLocators.ACTIVE_TAB)
        )
        self.highlight_element(driver, active_tab, 3)

        assert active_tab.find_element(*ConstructorPageLocators.BUNS_TEXT).is_displayed(), \
            "После возврата должен быть активен таб 'Булки'"