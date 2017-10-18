# todo: Итераторы

s = 'Linus Torvalds'
lst = [1, 2, 3, 4, 5]
person = {
    'name': 'Linus Torvalds',
    'age': 47,
    'is_developer': True
}

# it = iter(s)
# it = iter(lst)
# it = iter(person)
# it = iter(person.items())
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
#
# for i in s:
#     print(i)
#
# it = iter(s)
# while True:
#     try:
#         i = next(it)
#         print(i)
#     except StopIteration:
#         break

"""
Методы словаря:
-keys() - возвращает объект класса dict_values.
-values() - возвращает объект класса dict_keys.
-items() - возвращает объект класса dict_items.
"""


# print(person.items())
#
# for key in person.values():
#     print(key)
#
# print(list(enumerate(lst)))
#
# for i, value in enumerate(lst):
#     print(i, value)

# todo: Генераторы


def generator():
    print('Шаг №1')
    yield 1
    print('Шаг №2')
    yield 2
    print('Шаг №3')
    # return 'Error message'


# gen = generator()
# print(gen)
# print(type(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
#
# for i in generator():
#     print(i)
#
#
# def countdown(n):
#     print('Генератор запустился!')
#
#     while n:
#         yield n
#         n -= 1
#
# for i in countdown(5):
#     print(i)

# Python2: xrange(), dict.iteritems()

# todo: Генераторы списков, словарей, множеств.
"""
[expression for item1 in iterable if conditional1
            for item2 in iterable if conditional2
            ...
            for itemN in iterable if conditionalN
"""

# Генератор списка
number = [[i, j] for i in range(10) if i % 2 == 0
          for j in range(10, 30) if (j + i) % 2 != 0]
print(number)
print(type(number))

# Генератор множества
lst = [1, 1, 2, 2, 3, 3]
s = {i for i in lst}
print(s)
print(type(s))

# Генератор словаря
keys = ['id', 'original_url', 'short_url']
value = [1, 'https://python.org', '/1']

data = {k: v for k, v in zip(keys, value)}
print(data)
print(type(data))

data1 = dict(zip(keys, value))
print(data1)
print(type(data1))

data = [
    {
        'id': 1,
        'name': 'Linus Torvalds',
        'is_developer': True
    },
    {
        'id': 2,
        'name': 'Richard Stolman',
        'is_developer': True
    },
    {
        'id': 1,
        'name': 'Linus Torvalds',
        'is_developer': True
    }
]

persons = {d['id']: d for d in data}
print(persons)

# Выражения - генераторы

point = ([i, j] for i in range(10) if i % 2 == 0
         for j in range(10, 30) if (j + i) % 2 != 0)
print(type(point))


# with open(__file__) as f:
#     lines = (line.strip() for line in f)
#     todos = (s.split('# todo: ').pop() for s in lines if s.startswith('# todo: '))
#
#     print(list(todos))

# todo: Сопрограммы


def coroutine(func):
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g

    return wrapper


@coroutine
def splitter(delimeter=None):
    print('Генератор готов к приему данных')

    result = None
    while True:
        print('wait...', result)
        s = (yield result)
        print(s, result)
        result = s.split(delimeter)


sp = splitter(', ')
# next(sp)

print(sp.send('A, B, C'))
print(sp.send('1, 2, 3'))

# sp.close() - djp,e;lftn bcrk.xtybt ПутукфещкУчше возбуждает исключение внутри сопраграммы
# sp.throw(RuntimeError, 'Тебе конец.')
