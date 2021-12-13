dictionary = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}

def translate(english):
    if english.islower():
        return dictionary.get(english)
    elif english.istitle:
        english = english.lower()
        return dictionary.get(english).title()

number = input('Введите число на английском от 0 до 10 прописью: ')
print(translate(number))