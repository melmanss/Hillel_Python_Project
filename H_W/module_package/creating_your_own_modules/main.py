from student import Student
from group import Group

def main():
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

    gr = Group('PD1')
    gr.add_student(st1)
    gr.add_student(st2)

    print("Група після додавання:")
    print(gr)
    print("-" * 20)

    assert gr.find_student('Jobs') == st1, "Помилка: Студент не знайдений або не збігається"
    assert gr.find_student('Jobs2') is None, "Помилка: Знайдено неіснуючого студента"

    print("Пошук успішний!")

    gr.delete_student('Taylor')
    print("\nГрупа після видалення Taylor:")
    print(gr)

    assert gr.find_student('Taylor') is None
    print("-" * 20)
    print("Всі тести пройдено!")

if __name__ == "__main__":
    main()