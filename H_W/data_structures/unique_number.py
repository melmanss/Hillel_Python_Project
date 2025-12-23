def find_unique_value(some_list):
    for item in some_list:
        if some_list.count(item) == 1:
            return item
    return None


print(find_unique_value([1, 2, 1, 1]))
print(find_unique_value([2, 3, 3, 3, 5, 5]))
print(find_unique_value([5, 5, 5, 2, 2, 0.5]))
