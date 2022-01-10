class ZeroInputCheck(Exception):

    def __init__(self, number1, number2, message='Вы хотите поделить на ноль. Введите другое число.'):
        self.number1 = number1
        self.number2 = number2
        self.message = message
        super().__init__(self.message)

number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))

if number2 != 0:
    result = number1 / number2
    print(result)
else:
    raise ZeroInputCheck(number1, number2)
