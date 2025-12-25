def get_persistence_root(number: int) -> int:
    """
    Перемножує цифри числа, доки результат не стане одноцифровим.

    Args:
        number (int): Вхідне ціле число.

    Returns:
        int: Отримане одноцифрове число (від 0 до 9).
    """
    res = number

    while res > 9:
        digits_product = 1
        for digit in str(res):
            digits_product *= int(digit)
        res = digits_product

    return res


user_input = int(input("Введіть ціле число: "))
result = get_persistence_root(user_input)

print(result)