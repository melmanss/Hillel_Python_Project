def common_elements() -> set:
    """
    Генерує два списки чисел у діапазоні до 100: кратні 3 та кратні 5.
    Знаходить спільні елементи для обох списків.

    Returns:
        set: Множина чисел, які одночасно кратні й 3, і 5.
    """
    list_multiples_of_3 = [i for i in range(100) if i % 3 == 0]
    list_multiples_of_5 = [i for i in range(100) if i % 5 == 0]

    set_3 = set(list_multiples_of_3)
    set_5 = set(list_multiples_of_5)

    intersection = set_3 & set_5

    return intersection


result = common_elements()
print(result)