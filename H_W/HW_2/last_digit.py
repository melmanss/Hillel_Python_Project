print("\n--- 5. Остання цифра числа ---")
try:

    num5 = int(input("Введіть ціле число: "))

    last_digit = abs(num5) % 10

    print(f"Остання цифра: {last_digit}")

except ValueError:

    print("Помилка: Введено некоректне ціле число.")
