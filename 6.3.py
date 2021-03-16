import csv
from itertools import zip_longest

list_users = []
list_hobby = []
with open("users.csv", encoding='utf-8') as f:
    reader_1 = csv.reader(f)
    for row in reader_1:
        list_users.append((" ".join(row)))

with open("hobby.csv", encoding='utf-8') as file:
    reader_2 = csv.reader(file)
    for num in reader_2:
        list_hobby.append((",".join(num)))

if len(list_users) >= len(list_hobby):
    print(dict(zip_longest(list_users, list_hobby)))
else:
    print('«1»')
