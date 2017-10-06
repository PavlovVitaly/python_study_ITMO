# Форматы данных

# Pickle - нативный python-формат
import pickle  # python2 =( -> six (модуль позволяющий писать код, совместимый с python2 и python3)

data = {
    'users': [
        {
            'id': 1,
            'name': 'Linus Torvalds',
            'skills': ('C++', 'C')
        },
        {
            'id': 2,
            'name': 'Richard Stallman',
            'skills': ('C', 'GNU')
        }
    ]
}

with open('users.pickle', 'wb') as f:
    pickle.dump(data, f)

with open('users.pickle', 'rb') as f:
    loaded_data = pickle.load(f)
    print(loaded_data)

# Json - JavaScript Object Notation

import json  # не сохраняет кортежи, преобразует их в списки.

# Только двойные кавычки в json файле.

with open('users.json', 'w') as f:
    json.dump(data, f, indent=4)

with open('users.json') as f:
    loaded_data = json.load(f)
    print(loaded_data)

# CSV

import csv

"""
id;name;skills
1;Linus Torvalds;C,C++
2;Richard Stallman;C,GNU
"""

with open('users.csv', 'w') as f:
    users = data.get('users', [])  # Если ключа нет возвращает [].
    fieldnames = users[0].keys()  # Никогда так не делай!

    writer = csv.DictWriter(f,
                            fieldnames=fieldnames)
    writer.writeheader()

    for user in users:
        writer.writerow(user)

with open('users.csv') as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row)

# ini, conf
# xml - Extended Markup Language (lxml - модуль, работает с html)
# xps

# ==========================

# SQLite3/2 - База данных в одном файле
