def calculator():
    print("Калькулятор")
    while True:
        try:
            num1 = float(input("Введіть перше число: "))
            break
        except ValueError:
            print("Неправильний ввід. Будь ласка, введіть коректне число.")
    while True:
        operation = input("Введіть операцію (+, -, *, /): ").strip()
        if operation in ('+', '-', '*', '/'):
            break
        else:
            print("Неправильна операція. Дозволені операції: +, -, *, /.")
    while True:
        try:
            num2 = float(input("Введіть друге число: "))
            break
        except ValueError:
            print("Неправильний ввід. Будь ласка, введіть коректне число.")
    print(f"\nОбчислення: {num1} {operation} {num2}")
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("ПОМИЛКА: неможливо ділити на нуль.")
            return
        else:
            result = num1 / num2
    if result is not None:
        print(f"Результат: {result}")
calculator()