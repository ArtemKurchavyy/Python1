from random import choice


def get_jokes(number, flag=True):
    while number > 0:
        ''' генерирует случайным образом значение переменных из списков'''
        a = choice(nouns)
        b = choice(adverbs)
        c = choice(adjectives)

        if flag:
            '''если флаг = true, добавляет шутку в список, при этом слова могут повторяться'''
            list_joke.append(f'{a} {b} {c}')
            '''декремент счетчика'''
            number -= 1
        else:
            '''если флаг != true, добавляет шутку в список'''
            list_joke.append(f'{a} {b} {c}')
            '''удаляет из списка элемент, являющийся частью добавленной шутки, не допуская повторов слов в шутках'''
            nouns.remove(a)
            adverbs.remove(b)
            adjectives.remove(c)
            '''декремент счетчика'''
            number -= 1


nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']
list_joke = []

get_jokes(5, False)
print(list_joke)
