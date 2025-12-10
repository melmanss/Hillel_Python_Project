print("\n--- 2. Середнє трьох чисел ---")
try:
    print("Введіть три числа, розділені пробілом (наприклад, 2 4 6):")
    input_str = input()
    numbers_str = input_str.split()
    if len(numbers_str) != 3:
        print("Помилка: Необхідно ввести рівно три числа.")
    else:
        a = float(numbers_str[0])
        b = float(numbers_str[1])
        c = float(numbers_str[2])
        average = (a + b + c) / 3
        print(f"Середнє: {average:.1f}")
except ValueError:
    print("Помилка: Введено некоректні дані для чисел.")