class Cell:
    def __init__(self, param):
        self.param = param

    def __add__(self, other):
        return Cell(self.param + other.param)

    def __sub__(self, other):
        return Cell(self.param - other.param if self.param - other.param >= 0 \
            else 'Операция недоступна')

    def __mul__(self, other):
        return Cell(self.param * other.param)

    def __floordiv__(self, other):
        return Cell(self.param // other.param if other.param != 0 \
            else 'Операция недоступна')

    def __truediv__(self, other):
        return Cell(self.param / other.param if other.param != 0 \
            else 'Операция недоступна')

    def make_order(self, n):
        for i in range(self.param // n):
            print('*' * n)
        print('*' * (self.param % n))


a = Cell(10)
b = Cell(5)

print((a + b).param)
print((a - b).param)
print((a * b).param)
print((a // b).param)
print((a / b).param)

a.make_order(3)