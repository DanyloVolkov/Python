import os

path_1 = input('Введите путь для создания папки: ')
os.chdir(path_1)

dir_name = input('Введите название папки: ')
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
else:
    dir_name = input('Папка с таким именем уже существует. Введите другое имя: ')
    os.mkdir(dir_name)

sub_num = int(input('Введите количество желаемых папок: '))
path_2 = path_1 + '\\' + dir_name
os.chdir(path_2)

for i in range(1, sub_num + 1):
    subfolder_name = input('Введите название папки: ')
    os.mkdir(subfolder_name)