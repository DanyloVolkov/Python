a_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, v in enumerate(a_list):
    if v.isdigit():
        a_list[i] = f'"{int(v):02}"'
    elif v[1:].isdigit():
        a_list[i] = f'"{v[0]}{int(v):02}"'
print(' '.join(a_list))
