import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if name == "main":
    password_length = int(input("Введите длину пароля: "))
    if password_length < 1:
        print("Длина пароля должна быть больше 0.")
    else:
        password = generate_password(password_length)
        print(f"Сгенерированный пароль: {password}")