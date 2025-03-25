import random

# Вспомогательная функция для генерации email
def generate_email():
    return f"user_{random.randint(100, 999)}@yandex.ru"

# Вспомогательная функция для генерации пароля
def generate_password():
    return f"pass{random.randint(100, 999)}"