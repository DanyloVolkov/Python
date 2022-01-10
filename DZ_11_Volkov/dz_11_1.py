class Date:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def to_int(cls, date):
        day, month, year = map(int, date.split('-'))
        return cls(print(day, month, year))

    @staticmethod
    def validate(date):
        day, month, year = map(int, date.split('-'))
        return 0<day<=31 and 1<=month<=12 and year<2999



user_input = input('Введите дату в формате dd-mm-yyyy: ')

print(Date.to_int(user_input))
print(Date.validate(user_input))
