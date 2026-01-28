from typing import Optional
from student import Student

class Group:
    """Клас, що описує групу студентів."""

    def __init__(self, number: str):
        self.number: str = number
        self.group: set[Student] = set()

    def add_student(self, student: Student) -> None:
        """Додає студента до групи."""
        self.group.add(student)

    def find_student(self, last_name: str) -> Optional[Student]:
        """Шукає студента за прізвищем."""
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name: str) -> None:
        """Видаляє студента з групи за прізвищем."""
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self) -> str:
        all_students = "\n".join([str(student) for student in self.group])
        return f'Номер групи: {self.number}\n{all_students}'