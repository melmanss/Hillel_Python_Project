def checkio(data: list) -> int:
    if not data:
        return 0

    sum_even_indices = sum(data[::2])
    return sum_even_indices * data[-1]


test_cases = [
    [0, 1, 7, 2, 4, 8],
    [1, 3, 5],
    [6],
    []
]

print("Результати:")
for lst in test_cases:
    result = checkio(lst)
    print(f"{str(lst):8} => {result}")