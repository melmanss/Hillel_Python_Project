print("\n--- 3. Перетворення хвилин у години ---")
try:
    total_minutes = int(input("Введіть кількість хвилин: "))

    if total_minutes < 0:
        print("Кількість хвилин не може бути від'ємною.")
    else:

        hours = total_minutes // 60

        minutes = total_minutes % 60

        print(f"{hours} години {minutes} хвилин")

except ValueError:

    print("Помилка: Введено некоректне ціле число.")
