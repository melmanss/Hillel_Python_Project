def move_last_to_first_short(input_list):
    if len(input_list) <= 1:
        return input_list
    return input_list[-1:] + input_list[:-1]


list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]
list_c = [11, 12, 13, 14, 15]
list_d = []
print(f"Перевірка: {list_a} => {move_last_to_first_short(list_a)}")
print(f"Перевірка: {list_b} => {move_last_to_first_short(list_b)}")
print(f"Перевірка: {list_c} => {move_last_to_first_short(list_c)}")
print(f"Перевірка: {list_d} => {move_last_to_first_short(list_d)}")