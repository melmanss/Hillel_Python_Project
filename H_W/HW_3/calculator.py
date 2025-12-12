def calculator():
    print("Калькулятор")
    num1 = None
    while num1 is None:
        try:
            num1 = float(input("Введіть перше число: "))
        except ValueError:
            print("ПОМИЛКА: Будь ласка, введіть коректне число.")
    operation = None
    allowed_operations = ('+', '-', '*', '/')
    while operation not in allowed_operations:
        operation = input("Введіть операцію (+, -, *, /): ").strip()
        if operation not in allowed_operations:
            print(
                "ПОМИЛКА: Неправильна операція. Дозволені операції: "
                "+, -, *, /."
            )
    num2 = None
    while num2 is None:
        try:
            num2 = float(input("Введіть друге число: "))
        except ValueError:
            print("ПОМИЛКА: Будь ласка, введіть коректне число.")
    print(f"\nОбчислення: {num1} {operation} {num2}")
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    def multiply(a, b):
        return a * b
    def divide(a, b):
        if b == 0:
            return "ПОМИЛКА: неможливо ділити на нуль."
        return a / b
    operation_map = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
    }
    calculation_function = operation_map[operation]
    result = calculation_function(num1, num2)
    if isinstance(result, str) and result.startswith("ПОМИЛКА"):
        print(result)
    else:
        print(f"Результат: {result}")
calculator()