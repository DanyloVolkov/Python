class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed, self.color, self.name, self.is_police = speed, color, name, is_police

    def go (self):
        print(f'{self.color} {self.name} едет')

    def stop (self):
        print(f'{self.color} {self.name} остановилась')

    def turned (self, direction):
        self.direction = direction
        print(f'{self.color} {self.name} поехал на{self.direction}')

    def show_speed (self):
        print(f'Скорость составляет: {self.speed}')

    def check(self):
        print(f'Машина полиции: {self.is_police}')

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed <= 60:
            print(f'Скорость допустима, {self.speed}км/ч')
        else:
            print(f'Скорость превышена: {self.speed}км/ч')

    def check(self):
        print(f'Машина полиции: {self.is_police}')

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed <= 40:
            print(f'Скорость допустима, {self.speed}км/ч')
        else:
            print(f'Скорость превышена: {self.speed}км/ч')

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

    def check(self):
        print(f'Машина полиции: {self.is_police}')

car = Car(50, 'черный', 'BMW')
town = TownCar (80, 'белый', 'RR')
sport = SportCar (150, 'красный', 'Ferrari')
work = WorkCar (35, 'синий', 'ГАЗ')
police = PoliceCar (40, 'белый', 'Skoda')

town.go()
town.turned('лево')
town.stop()
town.show_speed()
town.check()