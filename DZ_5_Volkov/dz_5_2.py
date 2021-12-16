import sys

number = int(input('Введите число: '))
nums_gen = (n for n in range(1, number, 2))
print(type(nums_gen), sys.getsizeof(nums_gen))
print(next(nums_gen))
print(next(nums_gen))