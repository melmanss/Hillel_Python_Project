def format_time(seconds: int) -> str:
    """
    Переводить кількість секунд у формат: дні, гг:хх:сс.

    Args:
        seconds (int): Кількість секунд (0 <= seconds < 8640000).

    Returns:
        str: Відформатований рядок часу.
    """
    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    if 11 <= days % 100 <= 14:
        days_word = "днів"
    elif days % 10 == 1:
        days_word = "день"
    elif 2 <= days % 10 <= 4:
        days_word = "дні"
    else:
        days_word = "днів"

    time_str = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

    return f"{days} {days_word}, {time_str}"


user_input = int(input("Введіть кількість секунд: "))

if 0 <= user_input < 8640000:
    print(format_time(user_input))
else:
    print("Число поза межами допустимого діапазону.")