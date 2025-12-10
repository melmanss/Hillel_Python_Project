print("\n--- 6. Периметр прямокутника ---")

try:

    length = float(input("Введіть довжину: "))
    width = float(input("Введіть ширину: "))

    if length <= 0 or width <= 0:
        print("Довжина і ширина мають бути додатними числами.")
    else:

        perimeter = 2 * (length + width)

        print(f"Периметр: {perimeter:.0f}" if perimeter == int(perimeter) else f"Периметр: {perimeter}")

except ValueError:

    print("Помилка: Введено некоректні числові дані.")
