class MainPageLocators:
    LOGIN_BUTTON = ("css selector", "button.button_button__33qZ0")
    PERSONAL_ACCOUNT_BUTTON = ("css selector", "a[href='/account']")

class LoginPageLocators:
    EMAIL_INPUT = ("css selector", "input.text.input__textfield[type='text']")
    PASSWORD_INPUT = ("css selector", "input.text.input__textfield[type='password'][name='Пароль']")
    LOGIN_BUTTON = ("css selector", "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")
    REGISTER_LINK = ("css selector", "a.Auth_link__1fOlj[href='/register']")
    FORGOT_PASSWORD_LINK = ("css selector", "a.Auth_link__1fOlj[href='/forgot-password']")

class RegistrationPageLocators:
    NAME_INPUT = ("xpath", "//label[text()='Имя']/following-sibling::input")  # Добавлено
    EMAIL_INPUT = ("xpath", "//label[text()='Email']/following-sibling::input")  # Обновлено
    PASSWORD_INPUT = ("xpath", "//label[text()='Пароль']/following-sibling::input")  # Обновлено
    REGISTER_BUTTON = ("css selector", "button.button_button__33qZ0")
    LOGIN_LINK = ("css selector", "a.Auth_link__1fOlj[href='/login']")
    PASSWORD_ERROR = ("xpath", "//p[contains(@class, 'input__error')]")

class ForgotPasswordPageLocators:
    LOGIN_LINK = ("css selector", "a.Auth_link__1fOlj[href='/login']")

class PersonalAccountLocators:
    LOGOUT_BUTTON = ("css selector", "button.button_button__33qZ0")
    PROFILE_LINK = ("css selector", "a[href='/account/profile']")