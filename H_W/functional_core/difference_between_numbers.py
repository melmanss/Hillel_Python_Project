from typing import Union


def difference(*args: Union[int, float]) -> Union[int, float]:
    """
    Знайти різницю між найбільшим і найменшим елементом.

    Якщо аргументів немає, функція повертає 0.
    """
    if not args:
        return 0

    max_val: Union[int, float] = max(args)
    min_val: Union[int, float] = min(args)

    result: Union[int, float] = max_val - min_val

    return round(result, 2)


print(difference(1, 2, 3))
print(difference(5, -5))
print(difference(10.2, -2.2, 0, 1.1, 0.5))
print(difference())