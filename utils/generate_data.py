import random
import string

def generate_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{username}@example.com"

def generate_password(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))