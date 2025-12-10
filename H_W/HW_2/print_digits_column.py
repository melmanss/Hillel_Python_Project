print("\n--- 7. Виведення числа в стовпчик ---")
try:

    num7 = int(input("Введіть 4-х значне ціле число: "))

    abs_num7 = abs(num7)

    if 1000 <= abs_num7 <= 9999:

        digit1 = abs_num7 // 1000

        remaining_3_digits = abs_num7 % 1000
        digit2 = remaining_3_digits // 100

        remaining_2_digits = abs_num7 % 100
        digit3 = remaining_2_digits // 10

        digit4 = abs_num7 % 10

        print(digit1)
        print(digit2)
        print(digit3)
        print(digit4)

    else:
        print("Помилка: Введене число не є 4-х значним.")

except ValueError:

    print("Помилка: Введено некоректне ціле число.")
