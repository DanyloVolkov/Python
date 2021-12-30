class Road:
    _mass = 1500 # в кг

    def __init__(self, length = int(input('Введите длинну дороги в метрах: ')),
                 width = int(input('Введите ширину дороги в метрах: ')),
                 thickness = int(input('Введите толщину покрова дороги в сантиметрах: '))):

        self.length = length
        self.width = width
        self.thickness = thickness

    def road_mass(self):
        mass = self.length * self.width * (self.thickness / 100) * self._mass
        return print(mass)

a = Road()
a.road_mass()