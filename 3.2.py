def thesaurus(*args):
    for name in args:
        if dict_names.get(name[0]):
            dict_names.get(name[0]).append(name)
        else:
            dict_names[name[0]] = [name]
    print(dict_names)


dict_names = {}

thesaurus('Инга', 'Игорь', 'Валерий', 'Василий', 'Михаил')
