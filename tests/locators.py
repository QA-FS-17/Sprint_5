from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    RECOVERY_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")

class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and contains(text(), 'Личный Кабинет')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")

class PersonalAccountLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(@class, 'Account_button__14Yp3') and contains(text(), 'Выход')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
    PROFILE_SECTION = (By.XPATH, "//a[contains(text(), 'Профиль')]")

class PasswordRecoveryPageLocators:
    RECOVERY_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")  # Добавлен этот локатор
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")
    RECOVER_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")

class ConstructorPageLocators:
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']")
    ACTIVE_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]")