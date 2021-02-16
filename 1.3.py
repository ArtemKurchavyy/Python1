list_number = []
number = 1
while number <= 20:
    list_number.append(number)
    number += 1

list_symbol = ['процент', 'процента', "процентов"]
for num in list_number:
    if num >= 5:
        print(num, list_symbol[2])
    elif 1 < num < 5:
        print(num, list_symbol[1])
    else:
        print(num, list_symbol[0])
