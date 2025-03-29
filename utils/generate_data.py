import random

def generate_email():
    """Генерация уникального email"""
    return f"user_{random.randint(100, 999)}@example.com"

def generate_password():
    """Генерация пароля (6+ символов)"""
    return f"pass{random.randint(1000, 9999)}"