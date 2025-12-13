
def calculator(num1, operation, num2):
    operation_map = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }

    if operation not in operation_map:
        return "ПОМИЛКА: Неправильна операція."

    if operation == '/' and num2 == 0:
        return "ПОМИЛКА: Ділення на нуль неможливе."

    try:
        return operation_map[operation](num1, num2)
    except Exception as e:
        return f"ПОМИЛКА: Сталася невідома помилка: {e}"


print("Калькулятор")

try:
    input_num1 = float(input("Введіть перше число: "))
    input_operation = input("Введіть операцію (+, -, *, /): ").strip()
    input_num2 = float(input("Введіть друге число: "))

    final_result = calculator(input_num1, input_operation, input_num2)

    if isinstance(final_result, str) and final_result.startswith("ПОМИЛКА"):
        print(final_result)
    else:
        print(f"\nРезультат: {input_num1} {input_operation} "
              f"{input_num2} = {final_result}")

except ValueError:
    print("ПОМИЛКА: Введено некоректне число.")