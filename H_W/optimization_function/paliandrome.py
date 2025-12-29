"""
Модуль для перевірки рядків на паліндром.
"""


def is_palindrome(text: str) -> bool:
    """
    Перевіряє, чи є рядок паліндромом без урахування регістру та символів.

    Args:
        text (str): Рядок для перевірки.

    Returns:
        bool: True, якщо це паліндром, False в іншому випадку.
    """
    cleaned_text: str = "".join(char.lower() for char in text if char.isalnum())

    return cleaned_text == cleaned_text[::-1]


user_text: str = input("Введіть рядок для перевірки: ")
result: bool = is_palindrome(user_text)

print(result)