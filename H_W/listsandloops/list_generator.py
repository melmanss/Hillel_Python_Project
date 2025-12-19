def select_three_elements(data: list) -> list:
    if len(data) < 3:
        raise ValueError("Список елементів.")

    return [
        data[0],
        data[2],
        data[-2]
    ]


test_cases = [
    [1, 2, 3, 4, 5, 6, 7, 9],
    [1, 1, 2, 1],
    [6, 3, 7]
]

print("Результати")
for original_list in test_cases:
    final_list = select_three_elements(original_list)

    print(f"{str(original_list):30}{final_list}")