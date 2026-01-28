from __future__ import annotations
from typing import Union


class Rectangle:
    """
    Клас для представлення прямокутника та виконання операцій над його площею.
    """

    width: Union[int, float]
    height: Union[int, float]

    def __init__(self, width: Union[int, float], height: Union[int, float]) -> None:
        """
        Ініціалізує прямокутник із заданою шириною та висотою.
        """
        self.width = width
        self.height = height

    def get_square(self) -> Union[int, float]:
        """
        Обчислює площу прямокутника.
        """
        return self.width * self.height

    def __eq__(self, other: object) -> bool:
        """
        Порівнює прямокутники за їхньою площею.
        """
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return False

    def __add__(self, other: Rectangle) -> Rectangle:
        """
        Створює новий прямокутник із сумарною площею.
        """
        if isinstance(other, Rectangle):
            new_square = self.get_square() + other.get_square()
            return Rectangle(self.width, new_square / self.width)
        raise TypeError("Операція доступна тільки для Rectangle")

    def __mul__(self, n: Union[int, float]) -> Rectangle:
        """
        Збільшує площу прямокутника в n разів.
        """
        if isinstance(n, (int, float)):
            return Rectangle(self.width, self.height * n)
        raise TypeError("Множник має бути числом")

    def __str__(self) -> str:
        """
        Повертає опис параметрів прямокутника.
        """
        return f"Rectangle(width={self.width}, height={self.height})"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

print("OK")