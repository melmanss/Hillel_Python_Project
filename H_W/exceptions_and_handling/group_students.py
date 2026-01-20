from typing import Optional


class Human:
    """Клас, що описує людину."""

    def __init__(self, gender: str, age: int, first_name: str, last_name: str):
        self.gender: str = gender
        self.age: int = age
        self.first_name: str = first_name
        self.last_name: str = last_name

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} років"


class Student(Human):
    """Клас, що описує студента, успадкований від класу Human."""

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book: str = record_book

    def __str__(self) -> str:
        return f"{super().__str__()}, Залікова книжка: {self.record_book}"


class Group:
    """Клас, що описує групу студентів."""

    def __init__(self, number: str):
        self.number: str = number
        self.group: set[Student] = set()

    def add_student(self, student: Student) -> None:
        """Додає студента до групи."""
        self.group.add(student)

    def find_student(self, last_name: str) -> Optional[Student]:
        """Шукає студента за прізвищем. Повертає об'єкт Student або None."""
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
        return f'Номер групи: {self.number}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

print(gr)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр'

gr.delete_student('Taylor')
print(gr)

gr.delete_student('Taylor')