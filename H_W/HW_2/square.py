print("\n--- 1. Квадрат числа ---")
try:
    num1 = float(input("Введіть число: "))

    square = num1 ** 2

    print(f"Квадрат числа: {square}")

except ValueError:

    print("Помилка: Введено некоректне число.")
