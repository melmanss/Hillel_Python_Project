from typing import Dict


class Product:
    """Опис товару, що продається в магазині."""

    def __init__(
        self,
        name: str,
        price: float,
        description: str,
        dimensions: str
    ) -> None:
        self.name: str = name
        self.price: float = price
        self.description: str = description
        self.dimensions: str = dimensions

    def __str__(self) -> str:
        return f"{self.name} ({self.price} грн/кг)"


class Customer:
    """Клас для зберігання персональних даних покупця."""

    def __init__(
        self,
        last_name: str,
        first_name: str,
        middle_name: str,
        phone: str
    ) -> None:
        self.last_name: str = last_name
        self.first_name: str = first_name
        self.middle_name: str = middle_name
        self.phone: str = phone

    def __str__(self) -> str:
        return (
            f"{self.last_name} {self.first_name[0]}.{self.middle_name[0]}. "
            f"({self.phone})"
        )


class Order:
    """Клас для формування замовлення та збереження його у файл."""

    def __init__(self, customer: Customer) -> None:
        self.customer: Customer = customer
        self.products: Dict[Product, float] = {}

    def add_product(self, product: Product, quantity: float = 1.0) -> None:
        """Додає товар до замовлення або збільшує його кількість."""
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def calculate_total(self) -> float:
        """Обчислює сумарну вартість усіх позицій у замовленні."""
        return sum(
            product.price * qty for product, qty in self.products.items()
        )

    def save_to_file(self, filename: str = "order.txt") -> None:
        """Зберігає інформацію про замовлення у текстовий файл."""
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.__str__())

    def __str__(self) -> str:
        items_list: str = "\n".join(
            [f" - {p.name}: {qty} кг х {p.price} грн"
             for p, qty in self.products.items()]
        )
        return (
            f"Замовлення для: {self.customer}\n"
            f"Склад кошика:\n{items_list}\n"
            f"Разом: {self.calculate_total()} грн"
        )


apple: Product = Product("Яблуко Гала", 30.0, "Солодке", "Середнє")
banana: Product = Product("Банан", 65.0, "Еквадор", "20 см")
mango: Product = Product("Манго", 150.0, "Екзотика", "Велике")

buyer: Customer = Customer("Іванов", "Іван", "Іванович", "+380671234567")

order: Order = Order(buyer)
order.add_product(apple, 2.5)
order.add_product(banana, 1.2)
order.add_product(mango, 3.0)

# Виведення в консоль
print(order)

# Збереження у файл
order.save_to_file("fruit_order.txt")