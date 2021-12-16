numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
uniq_numbers = [n for n in numbers if numbers.count(n) == 1]
print(uniq_numbers)