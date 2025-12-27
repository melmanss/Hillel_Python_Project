"""
Модуль для математичних операцій над списками цифр.
"""


def add_one(digits: list[int]) -> list[int]:
    """
    Збільшує число, представлене списком цифр, на одиницю.

    Args:
        digits (list[int]): Список цифр, що складають число.

    Returns:
        list[int]: Список цифр отриманої суми.
    """
    number_str: str = "".join(map(str, digits))

    total: int = int(number_str) + 1

    result: list[int] = [int(d) for d in str(total)]

    return result


user_input: str = input("Введіть цифри через кому (наприклад, 1,2,3,4): ")
input_list: list[int] = [int(x.strip()) for x in user_input.split(",")]

final_result: list[int] = add_one(input_list)
print(final_result)