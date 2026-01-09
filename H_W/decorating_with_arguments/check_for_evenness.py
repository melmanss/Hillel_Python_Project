def is_even(num: int) -> bool:
    """
    Перевірити, чи є ціле число парним.

    Повертає True, якщо число ділиться на 2 без остачі, і False в іншому випадку.
    """
    result: bool = num % 2 == 0
    return result


try:
    user_input: str = input("Введіть ціле число: ")
    number: int = int(user_input)

    is_num_even: bool = is_even(number)
    print(is_num_even)
except ValueError:
    print("Помилка: введено не ціле число.")