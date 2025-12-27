"""
Модуль для пошуку другого входження підрядка.
"""


def second_index(text: str, symbol: str) -> int | None:
    """
    Знаходить індекс другого входження підрядка у рядку.

    Args:
        text (str): Рядок для пошуку.
        symbol (str): Підрядок, який потрібно знайти.

    Returns:
        int | None: Індекс другого входження або None, якщо його не існує.
    """
    first_idx: int = text.find(symbol)

    if first_idx == -1:
        return None

    second_idx: int = text.find(symbol, first_idx + len(symbol))

    return second_idx if second_idx != -1 else None


input_text: str = input("Введіть рядок: ")
input_symbol: str = input("Введіть шуканий підрядок: ")

result: int | None = second_index(input_text, input_symbol)

print(result)