def checkio(data: list) -> int:
    return data and sum(data[::2]) * data[-1] or 0


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