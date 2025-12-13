def calculator():
    print("Калькулятор")

    operation_map = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }

    try:
        num1 = float(input("Введіть перше число: "))
        operation = input("Введіть операцію (+, -, *, /): ").strip()
        num2 = float(input("Введіть друге число: "))

        if operation not in operation_map:
            print("ПОМИЛКА: Неправильна операція.")
            return

        if operation == '/' and num2 == 0:
            print("ПОМИЛКА: Ділення на нуль неможливе.")
            return

        result = operation_map[operation](num1, num2)

        print(f"\nРезультат: {num1} {operation} {num2} = {result}")

    except ValueError:
        print("ПОМИЛКА: Введено некоректне число.")
    except Exception as e:
        print(f"Сталася невідома помилка: {e}")


calculator()