"""
Модуль для модифікування рядків.
"""


def correct_sentence(text: str) -> str:
    """
    Виправляє речення: велика літера на початку та крапка в кінці.

    Args:
        text (str): Вхідний рядок.

    Returns:
        str: Виправлена копія рядка.
    """
    corrected: str = text[0].upper() + text[1:]

    if not corrected.endswith("."):
        corrected += "."

    return corrected


user_input: str = input("Введіть речення: ")
result: str = correct_sentence(user_input)

print(result)