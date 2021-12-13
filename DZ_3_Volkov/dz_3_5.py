nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

from random import choice

count = int(input('Введите количество желаемых шуток: '))
joke_list = []
def get_jokes(c):
    i = 0
    while i < count:
        noun = choice(nouns)
        adv = choice(adverbs)
        adj = choice(adjectives)
        joke = ' '.join([noun, adv, adj])
        joke_list.append(joke)
        i += 1

get_jokes(count)
print(joke_list)