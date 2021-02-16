list_cube = []
number = 0
while number <= 1000:
    if number % 2 != 0:
        list_cube.append(number ** 3)
    number += 1

result = 0
for num in list_cube:
    s = 0
    while num != 0:
        s += num % 10
        num = num // 10
        if s % 7 == 0:
            result = result + num
print(result)

result = 0
for num in list_cube:
    num = num + 17
    s = 0
    while num != 0:
        s += num % 10
        num = num // 10
        if s % 7 == 0:
            result = result + num
print(result)
