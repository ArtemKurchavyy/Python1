src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = []
unique_numbers = set()
repeating_numbers = set()

for el in src:
    if el not in repeating_numbers:
        unique_numbers.add(el)
    else:
        unique_numbers.discard(el)
    repeating_numbers.add(el)

sort = [result.append(num) for num in src if num in unique_numbers]


print(result)
