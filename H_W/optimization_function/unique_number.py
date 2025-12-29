"""
Модуль для пошуку унікального числа у списку.
"""


def find_unique_value(numbers: list[int]) -> int | None:
    """
    Знаходить число, яке зустрічається у списку лише один раз.

    Args:
        numbers (list[int]): Список цілих чисел.

    Returns:
        int | None: Унікальне число або None, якщо таке не знайдено.
    """
    for num in numbers:
        if numbers.count(num) == 1:
            return num

    return None


user_input: str = input("Введіть числа через пробіл: ")
input_list: list[int] = [int(x) for x in user_input.split()]

result: int | None = find_unique_value(input_list)
print(result)