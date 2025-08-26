class RegistrationPageLocators:
    NAME_INPUT = ("xpath", "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = ("xpath", "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = ("xpath", "//label[text()='Пароль']/following-sibling::input")
    REGISTER_BUTTON = ("css selector", "button.button_button__33qZ0")
    LOGIN_LINK = ("css selector", "a.Auth_link__1fOlj[href='/login']")
    PASSWORD_ERROR = ("xpath", "//p[contains(@class, 'input__error')]")

class MainPageLocators:
    LOGIN_BUTTON = ("css selector", "button.button_button__33qZ0")
    PERSONAL_ACCOUNT_BUTTON = ("css selector", "a[href='/account']")
    CONSTRUCTOR_BUTTON = ("css selector", "p.AppHeader_header__linkText__3q_va")
    LOGO_BUTTON = ("css selector", "div.AppHeader_header__logo__2D0X2")

class LoginPageLocators:
    EMAIL_INPUT = ("css selector", "input.text.input__textfield[type='text']")
    PASSWORD_INPUT = ("css selector", "input.text.input__textfield[type='password'][name='Пароль']")
    LOGIN_BUTTON = ("css selector", "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")

class PersonalAccountLocators:
    LOGOUT_BUTTON = ("css selector", "button.Account_button__14Yp3")
    PROFILE_LINK = ("css selector", "a[href='/account/profile']")

class ForgotPasswordPageLocators:
    LOGIN_LINK = ("css selector", "a.Auth_link__1fOlj[href='/login']")
    EMAIL_INPUT = ("css selector", "input[name='name']")
    RESET_BUTTON = ("css selector", "button.button_button__33qZ0")


class ConstructorPageLocators:
    # Основные локаторы текста табов
    BUNS_TEXT = ("xpath", "//span[@class='text text_type_main-default' and text()='Булки']")
    SAUCES_TEXT = ("xpath", "//span[@class='text text_type_main-default' and text()='Соусы']")
    FILLINGS_TEXT = ("xpath", "//span[@class='text text_type_main-default' and text()='Начинки']")

    # Локаторы родительских элементов табов для клика
    BUNS_TAB = ("xpath", "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Булки']/..")
    SAUCES_TAB = ("xpath", "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Соусы']/..")
    FILLINGS_TAB = ("xpath", "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Начинки']/..")

    # Локатор активного таба
    ACTIVE_TAB = ("xpath", "//div[contains(@class, 'tab_tab_type_current__2BEPc')]")
