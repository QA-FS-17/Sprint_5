from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def test_constructor_sections(driver):
    # Открываем главную страницу
    driver.get("https://stellarburgers.nomoreparties.site")

    # Ожидаем, пока страница полностью загрузится
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]"))
    )

    # Проверяем раздел "Булки"
    buns_section = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Булки']"))
    )
    # Прокручиваем страницу до элемента (если необходимо)
    driver.execute_script("arguments[0].scrollIntoView();", buns_section)
    # Используем ActionChains для клика
    ActionChains(driver).move_to_element(buns_section).click().perform()

    # Проверяем, что раздел "Булки" активен
    buns_active = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Булки']"))
    )
    assert "tab_tab_type_current__2BEPc" in buns_active.find_element(By.XPATH, "./..").get_attribute("class"), "Раздел 'Булки' не активен"

    # Проверяем раздел "Соусы"
    sauces_section = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Соусы']"))
    )
    # Прокручиваем страницу до элемента (если необходимо)
    driver.execute_script("arguments[0].scrollIntoView();", sauces_section)
    # Используем ActionChains для клика
    ActionChains(driver).move_to_element(sauces_section).click().perform()

    # Проверяем, что раздел "Соусы" активен
    sauces_active = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Соусы']"))
    )
    assert "tab_tab_type_current__2BEPc" in sauces_active.find_element(By.XPATH, "./..").get_attribute("class"), "Раздел 'Соусы' не активен"

    # Проверяем раздел "Начинки"
    fillings_section = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Начинки']"))
    )
    # Прокручиваем страницу до элемента (если необходимо)
    driver.execute_script("arguments[0].scrollIntoView();", fillings_section)
    # Используем ActionChains для клика
    ActionChains(driver).move_to_element(fillings_section).click().perform()

    # Проверяем, что раздел "Начинки" активен
    fillings_active = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Начинки']"))
    )
    assert "tab_tab_type_current__2BEPc" in fillings_active.find_element(By.XPATH, "./..").get_attribute("class"), "Раздел 'Начинки' не активен"