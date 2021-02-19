list_cost = sorted([53.2, 45.67, 97,  89.07, 34.5, 68.34, 90.11, 46.03, 77.2, 89.56, 33.9])
print(sorted(list_cost, reverse=True))
i = 5
for number in list_cost:
    if number == list_cost[-i]:
        if len(str(number)) > 2:
            element = str(number).split('.')
            if len(element[-1]) < 2:
                element[-1] = f'{element[-1]}0'
        else:
            element = [str(number), str(0)]
            element[-1] = f'{element[-1]}0'
        i -= 1
        print(f'{element[0]} руб. {element[1]} коп.', sep=' ', end=', ')

