"""
Модуль привітання користувача.

Цей скрипт запитує ім'я та вік користувача через термінал
і виводить форматоване привітання.
"""


def say_hi(name: str, age: int) -> str:
    """
    Представити людину за переданими параметрами.

    Args:
        name (str): Ім'я людини.
        age (int): Вік людини.

    Returns:
        str: Сформований рядок привітання.
    """
    greeting: str = f"Hi. My name is {name} and I'm {age} years old"
    return greeting

user_name: str = input("Введіть ваше ім'я: ")

user_age: int = int(input("Введіть ваш вік: "))

print(say_hi(user_name, user_age))