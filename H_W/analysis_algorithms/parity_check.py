def is_even(number: int) -> bool:
    """
    Перевіряє, чи є ціле число парним, використовуючи побітові операції.

    Args:
        number: Ціле число для перевірки.

    Returns:
        True, якщо число парне, і False, якщо непарне.
    """
    return (number & 1) == 0


try:
    user_input = input("Введіть ціле число: ")
    num = int(user_input)
    print(is_even(num))
except ValueError:
    print("Помилка: введено не ціле число.")