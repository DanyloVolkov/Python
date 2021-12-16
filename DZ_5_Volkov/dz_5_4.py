numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
for i, v in enumerate(numbers):
    if numbers[i] > numbers[i-1]:
        result.append(numbers[i])
result.pop(0)
print(result)