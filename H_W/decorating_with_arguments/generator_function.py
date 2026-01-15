from typing import Callable, Iterator


def pow_func(x: int) -> int:
    """Обчислити квадрат числа."""
    return x ** 2


def some_gen(begin: int, end: int, func: Callable[[int], int]) -> Iterator[int]:
    """
    Генератор числової послідовності.

    :param begin: Перший елемент послідовності.
    :param end: Кількість елементів у послідовності.
    :param func: Функція, яка формує наступне значення.
    """
    res: int = begin
    for _ in range(end):
        yield res
        res = func(res)


user_start: int = int(input("Введіть початкове число: "))
user_count: int = int(input("Введіть кількість елементів: "))

gen: Iterator[int] = some_gen(user_start, user_count, pow_func)

for value in gen:
    print(value)