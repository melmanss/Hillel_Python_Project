def move_zeros(lst):
    non_zeros = [x for x in lst if x != 0]
    zeros_count = len(lst) - len(non_zeros)
    result = non_zeros + [0] * zeros_count
    return result


example1 = [0, 1, 0, 12, 3]
example2 = [0]
example3 = [1, 0, 13, 0, 0, 0, 5]
example4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

print(f"{example1} -> {move_zeros(example1)}")
print(f"{example2} -> {move_zeros(example2)}")
print(f"{example3} -> {move_zeros(example3)}")
print(f"{example4} -> {move_zeros(example4)}")
