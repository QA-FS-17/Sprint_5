# Локаторы для главной страницы Stellar Burgers

# Контейнер с табами (разделами: Булки, Соусы, Начинки)
TABS_CONTAINER = "//div[contains(@class, 'tab_tab__1SPyG')]"

# Контейнер с табами

# Раздел "Булки"
BUNS_SECTION = "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Булки']"  # Кнопка раздела "Булки"
BUNS_ACTIVE = "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Булки']"  # Активный раздел "Булки"

# Раздел "Соусы"
SAUCES_SECTION = "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Соусы']"  # Кнопка раздела "Соусы"
SAUCES_ACTIVE = "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Соусы']"  # Активный раздел "Соусы"

# Раздел "Начинки"
FILLINGS_SECTION = "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Начинки']"  # Кнопка раздела "Начинки"
FILLINGS_ACTIVE = "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Начинки']"  # Активный раздел "Начинки"


# Локаторы для теста навигации Stellar Burgers

# Кнопка "Конструктор"
CONSTRUCTOR_BUTTON = "//p[contains(text(), 'Конструктор')]"  # Кнопка перехода в конструктор

# Кнопка "Войти в аккаунт"
LOGIN_BUTTON = "//button[text()='Войти в аккаунт']"  # Кнопка перехода на страницу входа

# Логотип "Stellar Burgers"
LOGO_BUTTON = "//div[contains(@class, 'AppHeader_header__logo__2D0X2')]"  # Логотип для перехода на главную страницу


# Локаторы для теста навигации в личный кабинет Stellar Burgers

# Поле ввода имени на странице регистрации
NAME_INPUT = "//input[@name='name']"  # Поле для ввода имени пользователя

# Поле ввода email на странице регистрации
EMAIL_INPUT_REGISTER = "//label[text()='Email']/following-sibling::input"  # Поле для ввода email при регистрации

# Поле ввода пароля на странице регистрации
PASSWORD_INPUT_REGISTER = "//label[text()='Пароль']/following-sibling::input"  # Поле для ввода пароля при регистрации

# Кнопка "Зарегистрироваться"
REGISTER_BUTTON = "//button[text()='Зарегистрироваться']"  # Кнопка для завершения регистрации

# Поле ввода email на странице входа
EMAIL_INPUT_LOGIN = "//input[@name='name']"  # Поле для ввода email при входе

# Поле ввода пароля на странице входа
PASSWORD_INPUT_LOGIN = "//input[@name='Пароль']"  # Поле для ввода пароля при входе

# Кнопка "Войти"
LOGIN_BUTTON = "//button[text()='Войти']"  # Кнопка для входа в аккаунт

# Кнопка "Личный кабинет"
PERSONAL_ACCOUNT_BUTTON = "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and contains(text(), 'Личный Кабинет')]"  # Кнопка перехода в личный кабинет


# Локаторы для теста регистрации с некорректным паролем Stellar Burgers

# Поле ввода имени на странице регистрации
NAME_INPUT = "//input[@name='name']"  # Поле для ввода имени пользователя

# Поле ввода email на странице регистрации
EMAIL_INPUT = "//label[text()='Email']/following-sibling::input"  # Поле для ввода email

# Поле ввода пароля на странице регистрации
PASSWORD_INPUT = "//label[text()='Пароль']/following-sibling::input"  # Поле для ввода пароля

# Кнопка "Зарегистрироваться"
REGISTER_BUTTON = "//button[text()='Зарегистрироваться']"  # Кнопка для завершения регистрации

# Сообщение об ошибке "Некорректный пароль"
ERROR_MESSAGE = "//p[contains(text(), 'Некорректный пароль')]"  # Сообщение об ошибке при некорректном пароле


# Локаторы для теста входа через главную страницу Stellar Burgers

# Кнопка "Войти в аккаунт" на главной странице
LOGIN_BUTTON = "//button[text()='Войти в аккаунт']"  # Кнопка для перехода на страницу входа

# Поле ввода email на странице входа
EMAIL_INPUT = "//input[@name='name']"  # Поле для ввода email

# Поле ввода пароля на странице входа
PASSWORD_INPUT = "//input[@name='Пароль']"  # Поле для ввода пароля

# Кнопка "Войти" на странице входа
SUBMIT_BUTTON = "//button[text()='Войти']"  # Кнопка для подтверждения входа


# Локаторы для теста входа через восстановление пароля Stellar Burgers

# Поле ввода имени на странице регистрации
NAME_INPUT = "//input[@name='name']"  # Поле для ввода имени пользователя

# Поле ввода email на странице регистрации
EMAIL_INPUT_REGISTER = "//label[text()='Email']/following-sibling::input"  # Поле для ввода email при регистрации

# Поле ввода пароля на странице регистрации
PASSWORD_INPUT_REGISTER = "//label[text()='Пароль']/following-sibling::input"  # Поле для ввода пароля при регистрации

# Кнопка "Зарегистрироваться"
REGISTER_BUTTON = "//button[text()='Зарегистрироваться']"  # Кнопка для завершения регистрации

# Поле ввода email на странице входа
EMAIL_INPUT_LOGIN = "//input[@name='name']"  # Поле для ввода email при входе

# Поле ввода пароля на странице входа
PASSWORD_INPUT_LOGIN = "//input[@name='Пароль']"  # Поле для ввода пароля при входе

# Кнопка "Войти"
LOGIN_BUTTON = "//button[text()='Войти']"  # Кнопка для подтверждения входа

# Кнопка "Личный кабинет"
PERSONAL_ACCOUNT_BUTTON = "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and contains(text(), 'Личный Кабинет')]"  # Кнопка перехода в личный кабинет

# Кнопка "Выйти"
LOGOUT_BUTTON = "//button[contains(@class, 'Account_button__14Yp3') and contains(text(), 'Выход')]"  # Кнопка выхода из аккаунта

# Кнопка "Восстановить пароль"
RECOVERY_BUTTON = "//a[text()='Восстановить пароль']"  # Кнопка перехода на страницу восстановления пароля

# Кнопка "Войти" на странице восстановления пароля
RECOVERY_LOGIN_BUTTON = "//a[text()='Войти']"  # Кнопка перехода на страницу входа со страницы восстановления пароля


# Локаторы для теста входа через личный кабинет Stellar Burgers

# Поле ввода email на странице входа
EMAIL_INPUT = "//input[@name='name']"  # Поле для ввода email

# Поле ввода пароля на странице входа
PASSWORD_INPUT = "//input[@name='Пароль']"  # Поле для ввода пароля

# Кнопка "Войти"
LOGIN_BUTTON = "//button[text()='Войти']"  # Кнопка для подтверждения входа

# Кнопка "Личный кабинет"
PERSONAL_ACCOUNT_BUTTON = "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and contains(text(), 'Личный Кабинет')]"  # Кнопка перехода в личный кабинет

# Кнопка "Выход"
LOGOUT_BUTTON = "//button[contains(@class, 'Account_button__14Yp3') and contains(text(), 'Выход')]"  # Кнопка выхода из аккаунта

# Кнопка "Конструктор"
CONSTRUCTOR_BUTTON = "//p[contains(text(), 'Конструктор')]"  # Кнопка перехода на главную страницу


# Локаторы для теста регистрации и входа Stellar Burgers

# Поле ввода имени на странице регистрации
NAME_INPUT = "//input[@name='name']"  # Поле для ввода имени пользователя

# Поле ввода email на странице регистрации
EMAIL_INPUT_REGISTER = "//label[text()='Email']/following-sibling::input"  # Поле для ввода email при регистрации

# Поле ввода пароля на странице регистрации
PASSWORD_INPUT_REGISTER = "//label[text()='Пароль']/following-sibling::input"  # Поле для ввода пароля при регистрации

# Кнопка "Зарегистрироваться"
REGISTER_BUTTON = "//button[text()='Зарегистрироваться']"  # Кнопка для завершения регистрации

# Поле ввода email на странице входа
EMAIL_INPUT_LOGIN = "//input[@name='name']"  # Поле для ввода email при входе

# Поле ввода пароля на странице входа
PASSWORD_INPUT_LOGIN = "//input[@name='Пароль']"  # Поле для ввода пароля при входе

# Кнопка "Войти"
LOGIN_BUTTON = "//button[text()='Войти']"  # Кнопка для подтверждения входа


# Локаторы для теста выхода из личного кабинета Stellar Burgers

# Поле ввода email на странице входа
EMAIL_INPUT = "//input[@name='name']"  # Поле для ввода email

# Поле ввода пароля на странице входа
PASSWORD_INPUT = "//input[@name='Пароль']"  # Поле для ввода пароля

# Кнопка "Войти"
LOGIN_BUTTON = "//button[text()='Войти']"  # Кнопка для подтверждения входа

# Кнопка "Личный кабинет"
PERSONAL_ACCOUNT_BUTTON = "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and contains(text(), 'Личный Кабинет')]"  # Кнопка перехода в личный кабинет

# Кнопка "Выход"
LOGOUT_BUTTON = "//button[contains(@class, 'Account_button__14Yp3') and contains(text(), 'Выход')]"  # Кнопка выхода из аккаунта


# Локаторы для теста успешной регистрации Stellar Burgers

# В данном тесте используется только проверка URL, поэтому отдельные локаторы для элементов не требуются.