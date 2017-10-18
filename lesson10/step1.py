# Декораторы
# gc.disable()
# gc.enable()

def tst(*args, **kwargs):
    print(type(args))
    print(type(kwargs))
    print(args)
    print(kwargs)


tst()
tst(1)
tst(prop=2)
tst(4, 5, prop2=8, key=9)

arguments = [1, 2, 3, 4, 5]
keyword_arguments = {
    'user': 'root',
    'password': 'toor'
}

tst(*arguments, **keyword_arguments)


def func():
    def wrapper():
        pass

    return wrapper


f = func()
print(type(f), f)

from urllib.request import urlopen


def page(url):
    def get():
        return urlopen(url).read()

    return get


python = page('https://python.org')
print(type(python), python)


def factorial(n):
    f = 1

    for i in range(1, n + 1):
        f *= i

    return f


import time


def benchmark(func, *args, **kwargs):
    started = time.time()
    result = func(*args, **kwargs)
    worked = time.time() - started
    print('Функция "{}" выполнилась за {:f} микросекунд.'.format(func.__name__, worked * 1e6))
    return result


print('Факториал 500 = ', benchmark(factorial, 5000))
