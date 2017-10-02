# Функции
def hello():
    print('Hello, Function!')


hello()
print(hello)
v = hello
v()


# Аргументы функции
def say_hello(name):
    print('Hello', name, '!')


say_hello('Vitaly')


def login(user='USER', password='PASSWORD'):
    template = 'Пользователь {} зашел с паролем {}.'
    msg = template.format(user, password)
    print(msg)


login('Vitaly', '123')
login('Vitaly')
login()
login(password='123')
login(password='123', user='Vitaly')


def parse(src, output):
    src = src.strip('.')  # удаляет символ с начала и с конца.
    for w in src.split():
        output.append(w)


src = 'Python is programming language...'
lst = []

parse(src, lst)
print(src, lst)


def pow(x, p=2):
    return x ** p


print(pow(2), pow(3, 8))


def create_func():
    def func():
        print('111')

    return func


a = create_func()
a()


# можно вернуть кортеж
def pow_tuple(x, p=2):
    return x ** p, x ** (2 * p), x ** (3 * p)


print(pow_tuple(2))
print(pow_tuple(2)[1])


def f(x, l=[]):  # ЗАПРЕЩЕНО!
    print(l)
    l.append(x)


f(1)
f(2)
f(3)
f(4, [])


def f(x, l=None):
    l = l or []  # как в java-script
    print(l)
    l.append(x)


def func2(x, y):
    return x - y


print(func2(y=8, x=5), func2(9, 6))


# Переменное кол-во аргументов
def summa(*args, start=0):
    """
    *args - позиционные аргументы (turtle)
    **kwargs - именованные аргументы (dictionary)
    """
    return sum(args[start:])


print(summa(1, 2, 3), summa(4, 10, 89, 78, 78), summa(2, 2))
print(summa(10, 2, 4, start=1))

login_data = ['user1', '1']
login(*login_data)

login_data_dict = {
    'user': 'user2',
    'password': '2'
}
login(**login_data_dict)

# Анонимная функция
sqrt = lambda x: x ** 0.5
print(sqrt(9))
print(sqrt)


#
# def func3(callback):
#     callable()
#
# func3(lambda: 'something')

# Замыкания
# Функция каррирования
def trim(chars=None):
    def func(s):
        return s.strip(chars)

    return func


trim_spaces = trim()
trim_slashes = trim('/\\|')
print(trim_spaces, trim_slashes)
print(trim_spaces('   hello   '))


# Python3 самое необходимое (Прохоренок - уг, не читай)
# Лутс

# Рекурсивная функция
def factorial(x):
    return 1 if x == 0 else x * factorial(x - 1)


print(factorial(5))

# Косвенная рекурсия
# def a():
#     b()
#
# def b():
#     a()

# Область видимости и время жизни переменной
# Глобальные переменные
# - все, кроме функций и классов
# Локальные переменные
# - тело функции
# - классы

g = 888  # глобальная
lst = []


def wrapper():
    # g = 777     # локальная
    # print(g)
    external = 777

    def func():
        global g  # нужно только в случае изменения
        # nonlocal external       # нужно только в случае изменения
        print(external)

    func()
    lst.append(456)


wrapper()
print(g)
print(lst)
