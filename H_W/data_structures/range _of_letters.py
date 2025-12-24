import string


def get_characters_between(range_str: str) -> str:
    """
    Повертає послідовність символів між двома заданими літерами включно.

    Args:
        range_str (str): Рядок у форматі "літера1-літера2".

    Returns:
        str: Рядок з усіх символів у діапазоні.
    """
    start_char, end_char = range_str.split("-")
    all_letters = string.ascii_letters

    start_index = all_letters.find(start_char)
    end_index = all_letters.find(end_char)

    return all_letters[start_index:end_index + 1]


user_input = input("Введіть через дефіс дві літери (наприклад, a-H): ")
result = get_characters_between(user_input)

print(result)