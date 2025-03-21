# Добавим фикстуру для настройки драйвера:

import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Настройка драйвера для Chrome
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()