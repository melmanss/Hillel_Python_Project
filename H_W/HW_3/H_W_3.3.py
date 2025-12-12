def split_list_into_two(input_list):
    n = len(input_list)
    if n == 0:
        return [[], []]
    first_list_length = (n + 1) // 2
    first_half = input_list[:first_list_length]
    second_half = input_list[first_list_length:]
    return [first_half, second_half]
test_cases = {"І": [1, 2, 3, 4, 5, 6], "ІІ": [1, 2, 3], "ІІІ": [1, 2, 3, 4, 5],
              "ІV": [1], "V": [], "VI": [10, 20, 30, 40]}
print("Результати:")
for case_name, input_list in test_cases.items():
    result = split_list_into_two(input_list)
    print(f"{case_name.ljust(15)} | Було: {input_list} \t=> Стало: {result}")