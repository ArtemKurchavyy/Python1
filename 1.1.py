second_answer = int(input('Введите количество секунд'))
second = second_answer % 60
minutes = second_answer // 60
hours = minutes // 60
day = hours // 24
years = day // 365
list_watch = [str(second), str(minutes % 60), str(hours % 24), str(day % 365), str(years)]
list_symbol = [' сек.', ' мин. ', ' час. ', ' сут. ', ' г. ']
if minutes > 0 and hours < 1:
    print('Это ', list_watch[1], list_symbol[1], list_watch[0], list_symbol[0])
elif hours > 0 and day < 1:
    print('Это ', list_watch[2], list_symbol[2], list_watch[1], list_symbol[1], list_watch[0],
          list_symbol[0])
elif day > 0 and years < 1:
    print('Это ', list_watch[3], list_symbol[3], list_watch[2], list_symbol[2], list_watch[1],
          list_symbol[1], list_watch[0], list_symbol[0])
elif years > 0:
    print('Это ', list_watch[4], list_symbol[4], list_watch[3], list_symbol[3], list_watch[2],
          list_symbol[2], list_watch[1], list_symbol[1], list_watch[0], list_symbol[0])
else:
    print('Это ', list_watch[0], list_symbol[0])
