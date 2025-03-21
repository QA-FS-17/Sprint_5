# Создадим генераторы для email и пароля:

import random

def generate_email():
    # Генерация email в формате имя_фамилия_номер_когорты_3цифры@домен
    return f"user_{random.randint(100, 999)}@example.com"

def generate_password():
    # Генерация пароля из 6 символов
    return f"pass{random.randint(100, 999)}"