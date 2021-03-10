from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
classes = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def generate_tuple():
    if len(tutors) > len(classes):
        for i, j in zip_longest(tutors, classes):
            yield i, j
    else:
        for i, j in zip(tutors, classes):
            yield i, j


a_gen = generate_tuple()

print(next(a_gen))
print(next(a_gen))
print(next(a_gen))
print(next(a_gen))
print(next(a_gen))
print(next(a_gen))
print(next(a_gen))
print(next(a_gen))
