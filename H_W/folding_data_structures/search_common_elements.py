def common_elements() -> set[int]:
    """
    Генерує два списки чисел у діапазоні до 100: кратні 3 та кратні 5.
    Знаходить спільні елементи для обох списків.

    Returns:
        set[int]: Множина чисел, які є спільними кратними.
    """
    multiples_3: set[int] = {i for i in range(0, 100, 3)}
    multiples_5: set[int] = {i for i in range(0, 100, 5)}

    return multiples_3 & multiples_5


result: set[int] = common_elements()
print(result)
