from typing import Iterator


def prime_generator(end: int) -> Iterator[int]:
    """
    Генерує прості числа від 2 до вказаної межі.

    Args:
        end: Верхня межа діапазону (включно).

    Yields:
        Наступне просте число в послідовності.
    """
    for num in range(2, end + 1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            yield num


try:
    user_limit = int(input("Введіть верхню межу діапазону: "))
    print(list(prime_generator(user_limit)))
except ValueError:
    print("Помилка: будь ласка, введіть ціле число.")