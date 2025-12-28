"""
Модуль для пошуку спільних елементів кратних 3 та 5.
"""


def common_elements() -> set[int]:
    """
        Знаходить числа до 100, які одночасно кратні 3 та 5.

        Returns:
            set[int]: Множина чисел, які є спільними кратними.
    """
    return set(range(0, 100, 3)) & set(range(0, 100, 5))


result: set[int] = common_elements()
print(result)