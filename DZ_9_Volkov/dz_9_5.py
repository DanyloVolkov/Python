class Stationery:
    title = 'Stationery'

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    title = 'Ручка'

    def draw(self):
        print(f'Рисуем {self.title}')


class Pencil(Stationery):
    title = 'Карандаш'

    def draw(self):
        print(f'Рисуем {self.title}')

class Marker(Stationery):
    title = 'Маркер'

    def draw(self):
        print(f'Рисуем {self.title}')

a = Stationery()
a.draw()

b = Pen()
b.draw()

c = Pencil()
c.draw()

d = Marker()
d.draw()