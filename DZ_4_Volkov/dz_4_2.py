from requests import get, utils

def currency_rate(value):
    link = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encodings_from_headers(link.headers)
    date = link.headers['Set-cookies'].split(',')[1]
    print(f'Дата: {date}')

    content = link.content.decode(encodings=encodings)
    key = ['Nominal', 'Name', 'Value']
    currency_str = content[content.find(str(value).upper()):]

    if len(currency_str) > 2:
        currency_str = currency_str[:currency_str.find('</Valute>')]
        currency_info = list(map(lambda x: str(currency_str.split(x)[1])[1:-2], key))
        currency_info[0] = int(currency_info[0])
        currency_info[2] = float('.'.join(currency_info[2].split(',')))

    else:
        print(None)


currency_rate(input('Введите нужню валюту: '))