prices = [57.8, 46.51, 97, 63.07, 23.18, 35.05, 48.3, 79.09, 100.9, 15.21]

#Зданине А
print('Задание А')
for i in prices:
    print(f'{int(i)} руб. {int(i * 100 % 100):02} коп.', end=' , ')
print('\n\n')

#Задание В
print('Задание В')
print('Ориг. список:', id(prices), prices)
prices.sort()
print('Сорт. список:', id(prices), prices)
print('\n')

#Задание С
print('Задание С')
prices_new = sorted(prices, reverse=True)
# prices_new.sort(reverse=True)
print('Новый список:', id(prices_new), prices_new)
print('\n')

#Задание D
print('Задание D')
prices.sort()
print(prices[-5:])

