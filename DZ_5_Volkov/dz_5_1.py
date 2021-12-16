import sys

def number_gen(number):
    for n in range(1, number, 2):
        yield n

number = int(input('Введите число: '))
nums_gen = number_gen(number)
print(type(nums_gen), sys.getsizeof(nums_gen))
print(next(nums_gen))
print(next(nums_gen))