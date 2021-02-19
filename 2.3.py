list_name = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']
for num in list_name:
    element = num.split(' ')
    name = element[-1].capitalize()
    print(f'Привет, {name}!')
