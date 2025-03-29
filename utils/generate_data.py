import random
import string

# Генерация тестовых данных
def generate_email():
    return f"user_{random.randint(1000, 9999)}@example.com"

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%"
    return ''.join(random.choice(chars) for _ in range(10))