import re

def log_filter(data):
    flt = [r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',
           r'\[(.*?)\]',
           r'\"([A-Z]{3})',
           r'\s(\/[\w\/]+)',
           r'\s(\d{3})\s',
           r'\s\d{3}\s(\d+)'
           ]
    return tuple(re.findall(x, data)[0] for x in flt)

with open('nginx_logs.txt', 'r', encoding='utf-8') as data:
    for line in data:
        print(log_filter(line))
