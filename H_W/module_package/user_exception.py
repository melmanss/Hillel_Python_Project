from typing import Optional


class GroupLimitError(Exception):
    """Виняток для обмеження кількості студентів у групі до 10 осіб."""

    def __init__(self, message: str = "У групі не може бути більше 10 студентів"):
        self.message: str = message
        super().__init__(self.message)


class Human:
    """Клас, що описує загальні характеристики людини."""

    def __init__(self, gender: str, age: int, first_name: str, last_name: str):
        self.gender: str = gender
        self.age: int = age
        self.first_name: str = first_name
        self.last_name: str = last_name

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} років"


class Student(Human):
    """Клас для опису студента, що наслідує властивості людини."""

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book: str = record_book

    def __str__(self) -> str:
        return f"{super().__str__()}, Залікова книжка: {self.record_book}"


class Group:
    """Клас для керування списком студентів у групі."""

    def __init__(self, number: str):
        self.number: str = number
        self.group: set[Student] = set()

    def add_student(self, student: Student) -> None:
        """Додає студента до групи. Викидає GroupLimitError, якщо студентів вже 10."""
        if len(self.group) >= 10:
            raise GroupLimitError(f"Неможливо додати {student.first_name} {student.last_name}. "
                                 f"Ліміт групи {self.number} вичерпано.")
        self.group.add(student)

    def find_student(self, last_name: str) -> Optional[Student]:
        """Шукає студента в групі за прізвищем. Повертає об'єкт або None."""
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name: str) -> None:
        """Видаляє студента з групи за прізвищем."""
        student: Optional[Student] = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self) -> str:
        all_students: str = "\n".join([str(student) for student in self.group])
        return f"Номер групи: {self.number}\n{all_students}"


gr: Group = Group('PD1')

try:
    for i in range(11):
        st: Student = Student('Male', 18 + i, f'Ім’я_{i}', f'Прізвище_{i}', f'Квиток_{i}')
        gr.add_student(st)
        print(f"Додано студента: {st.last_name}")
except GroupLimitError as e:
    print(f"\nПомилка: {e}")

print("\nФінальний склад групи:")
print(gr)