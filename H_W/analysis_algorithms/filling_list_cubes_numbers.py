from typing import Iterator


def generate_cube_numbers(end: int) -> Iterator[int]:
    """
    Генерує куби чисел, починаючи з 2, доки значення не перевищує межу.

    Args:
        end: Верхня межа для значень кубів (включно).

    Yields:
        Куб чергового цілого числа (num ** 3).
    """
    num = 2
    while True:
        cube = num ** 3
        if cube > end:
            return
        yield cube
        num += 1


try:
    user_limit = int(input("Введіть верхню межу для кубів: "))
    print(list(generate_cube_numbers(user_limit)))
except ValueError:
    print("Помилка: введено не ціле число.")