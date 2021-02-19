list_symbol = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for num in list_symbol:
    if num.isdigit() and len(num) < 2:
        list_symbol.insert(list_symbol.index(num) + 1, '"')
        list_symbol.insert(list_symbol.index(num), '"')
        list_symbol[list_symbol.index(num)] = f'0{num}'
    elif num[0] == '+' and len(num) < 3:
        list_symbol.insert(list_symbol.index(num) + 1, '"')
        list_symbol.insert(list_symbol.index(num), '"')
        list_symbol[list_symbol.index(num)] = f'+0{num[1:]}'
    elif list_symbol[list_symbol.index(num) - 1] != '"' and num.isdigit():
        list_symbol.insert(list_symbol.index(num) + 1, '"')
        list_symbol.insert(list_symbol.index(num), '"')

print(list_symbol)

line = (f'{list_symbol[0]} {list_symbol[1]}{list_symbol[2]}{list_symbol[3]} {list_symbol[4]} {list_symbol[5]}'
        f'{list_symbol[6]}{list_symbol[7]} {list_symbol[8]} {list_symbol[9]} {list_symbol[10]} {list_symbol[11]} '
        f'{list_symbol[12]}{list_symbol[13]}{list_symbol[14]} {list_symbol[15]}')

print(line)
