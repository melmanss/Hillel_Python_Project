print("\n--- 4. Розрахунок знижки ---")
try:
    price = float(input("Введіть ціну: "))
    discount_percent = float(input("Введіть знижку (%): "))
    if price < 0 or discount_percent < 0:
        print("Ціна та знижка не можуть бути від'ємними.")
    else:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        print(f"Ціна зі знижкою: {final_price:.1f}")
except ValueError:
    print("Помилка: Введено некоректні числові дані.")