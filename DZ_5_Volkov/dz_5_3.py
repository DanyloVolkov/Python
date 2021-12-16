from itertools import zip_longest, islice
import sys

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 'Ирина',
    'Дмитрий', 'Борис', 'Елена', 'Василий', 'Владимир',
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

generator = ((tutors, klasses) for tutors, klasses in zip_longest(tutors, klasses))
print(generator)
print(*islice(generator, len(tutors)), sep = '\n')
print(type(generator), sys.getsizeof(generator))
