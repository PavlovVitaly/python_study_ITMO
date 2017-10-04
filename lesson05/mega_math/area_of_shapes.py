from math import pi as PI

sss = 1


def calculate_area_of_square(a):
    """
    Возвращает площадь квадрата.
    :param a:
    :return:
    """
    return a ** 2


def calculate_area_of_rectangle(a, b):
    """
    Возвращает площадь прямоугольника.
    :param a:
    :param b:
    :return:
    """
    return a * b * sss


def calculate_area_of_circle(r):
    """
    Возвращает площадь круга.
    :param r:
    :return:
    """
    return PI * r ** 2


# Список того, что будет импортировано.
__all__ = [
    'calculate_area_of_circle',
    'calculate_area_of_rectangle',
    'calculate_area_of_square'
]
