class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.real == 0 and self.imag ==0:
            return f'{str(self.real)}'
        elif (self.real > 0 or self.real < 0) and self.imag == 0:
            return f'{str(self.real)}'
        elif (self.imag > 0 or self.imag < 0) and self.real == 0:
            return f'{str(self.imag)}i'
        elif self.imag > 0:
            return f'{str(self.real)}+{str(self.imag)}i'
        elif self.imag < 0:
            return f'{str(self.real)}{str(self.imag)}i'

    def __add__(self, other):
        real_num = self.real + other.real
        imag_num = self.imag + other.imag
        if real_num == 0 and imag_num == 0:
            return f'{str(real_num)}'
        elif (real_num > 0 or real_num < 0) and imag_num == 0:
            return f'{str(real_num)}'
        elif (imag_num > 0 or imag_num < 0) and real_num == 0:
            return f'{str(imag_num)}i'
        elif imag_num > 0:
            return f'{str(real_num)}+{str(imag_num)}i'
        elif imag_num < 0:
            return f'{str(real_num)}{str(imag_num)}i'

    def __mul__(self, other):
        real_num = self.real * other.real - self.imag * other.imag
        imag_num = self.real * other.imag + self.imag * other.real
        if real_num == 0 and imag_num == 0:
            return f'{str(real_num)}'
        elif (real_num > 0 or real_num < 0) and imag_num == 0:
            return f'{str(real_num)}'
        elif (imag_num > 0 or imag_num < 0) and real_num == 0:
            return f'{str(imag_num)}i'
        elif imag_num > 0:
            return f'{str(real_num)}+{str(imag_num)}i'
        elif imag_num < 0:
            return f'{str(real_num)}{str(imag_num)}i'

number_1 = Complex(2, -5)
number_2 = Complex(3, 1)

print(f'Введенные числа: {number_1} и {number_2}')
print('Сложение чисел:',number_1 + number_2)
print('Умножение чисел:',number_1 * number_2)