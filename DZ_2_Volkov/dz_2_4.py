workers = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in workers:
    name = i.split(' ')[-1].capitalize()
    print(f'Привет, {name}!')
