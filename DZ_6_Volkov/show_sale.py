import sys

if __name__ == '__main__':
    interval = list(map(int, sys.argv[1:]))
    with open('bakery.cvs', 'r', encoding='utf-8') as file:
        text = file.readlines()
        if len(interval) == 2:
            for line in text[interval[0] - 1:interval[1]]:
                print(line.strip())
        elif len(interval) == 1:
            for line in text[interval[0] - 1]:
                print(line.strip())
        else:
            for line in text:
                print(line.strip())
    exit()