def num_translate(num):
    if numbers.get(num.lower()):
        for key, val in numbers.items():
            if key == num:
                print(val)
            elif key.capitalize() == num:
                print(val.capitalize())
    else:
        print('None')


numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
           'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

num_translate('one')
num_translate('Six')
num_translate('eleven')
