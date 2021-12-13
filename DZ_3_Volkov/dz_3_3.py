def thesaurus(*args):
    keys = sorted(set(x[0] for x in args))
    thesaurus_names = dict()
    for i in keys:
        thesaurus_names[i] = list(filter(lambda x: x[0] == i, args))
    return  thesaurus_names

print(thesaurus('Сергей', 'Иван', 'Павел', 'Яна', 'Андрей', 'Василий', 'Ян', 'Петр', 'Савелий'))