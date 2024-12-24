import re

addresses = [
    ('Он проживал в городе Иваново на улице Наумова. ' 
     'Номер дома 125 был зеркальной копией его номера квартиры 521'),
    'Адрес: город Новосибирск, улица Фрунзе, дом 321, квартира 15.'
]

for address in addresses:
    # Напишите регулярное выражение.
    pattern = r'(?:город.+?(?P<city>\w+))|(?:дом.+?(?P<home>\d+))|(?:квартир.+ (?P<flat>\d+))|(?:улиц.?.(?P<line>\w+))'

    matches = re.finditer(pattern, address)

    res = []

    for match in matches:
        if match.group('city'):
            res.append(match.group('city'))
        if match.group('line'):
            res.append(match.group('line'))
        if match.group('home'):
            res.append(match.group('home'))
        if match.group('flat'):
            res.append(match.group('flat'))

    print(' '.join(res))
