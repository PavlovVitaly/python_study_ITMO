import pickle
import time
from datetime import datetime
from functools import reduce, wraps


#
# def decorator(func):
#     # Всегда должен вернуть функцию обертку.
#     def wrapper(*args, **kwargs):
#         # Внутри обертки необходимо вызвать декорируемую функцию.
#         # Действия до вызова
#         result = func(*args, **kwargs)
#         # Действия после вызова
#         return func
#     return wrapper
#
#
# @decorator
# def tst():
#     pass
#
#
# # tst = decorator(tst)
# tst()


def benchmark(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        started = time.time()
        result = func(*args, **kwargs)
        worked = time.time() - started
        print('Функция "{}" выполнилась за {:f} микросекунд.'.format(func.__name__, worked * 1e6))
        return result

    return wrapper


def cache(func):
    """functools.lru_cache"""
    memory = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = pickle.dumps((args, sorted(kwargs.items())))
        if key not in memory:
            memory[key] = func(*args, **kwargs)
        return memory[key]

    return wrapper


# Декораторы с параметрами
"""
Функция log() принимает параметры декоратора и возвращает декоратор
"""


def log(filename):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            template = '''
[{now:%Y-%m-%d %H:%M:%S}] Function: "{func}" called with:
    -> positional arguments:    {args}
    -> keyword arguments:       {kwargs}
Returns: {result}         
'''
            with open(filename, 'a') as f:
                f.write(template.format(now=datetime.now(),
                                        func='.'.join([func.__module__, func.__name__]),
                                        args=args,
                                        kwargs=kwargs,
                                        result=result))
            return result

        return wrapper

    return decorator


@log('log.txt')
@benchmark
@cache
# @lru_cache(25)
def factorial(n):
    return reduce(lambda f, x: f * x, range(1, n + 1))


print('Факториал 500 = ', factorial(5000))
print('Факториал 500 = ', factorial(5000))
print('Факториал 500 = ', factorial(5000))

print(factorial)
