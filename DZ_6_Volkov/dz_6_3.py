from itertools import zip_longest

with open('users.csv', 'r', encoding= 'utf-8') as name, \
        open('hobby.csv', 'r', encoding='utf-8') as hobby:
    names = name.read().splitlines()
    hobbies = hobby.read().splitlines()

user_hobby_generator = ((names, hobbies) for names, hobbies in zip_longest(names, hobbies))

with open('users_hobby.txt', 'w', encoding='utf-8') as final_list:
    for i in user_hobby_generator:
        final_list.write(f'{i[0]}: {i[1]}\n')