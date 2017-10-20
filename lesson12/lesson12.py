"""
Классы и объекты

Метод - функция, объявленная в контексте класса.
      - поведение
Свойства - функция, объявленная в контексте класса.
         - поведение
"""


# Классы в CamelCase


class Person():
    def __init__(self, firstname, lastname):
        """
        Метод конструктор
        Основная цель конструктора - инициализирующий объект.
        self - ссылка на текущий экземпляр или объект.
        """
        self.firstname = firstname
        self.lastname = lastname

    def print_info(self):
        pass


class Developer(Person):
    def __init__(self, firstname, lastname, skills):
        super().__init__(firstname, lastname)
        self.skills = skills

    def print_inf(self):
        super().print_info()


person_1 = Person('Dredd', 'Noteee')
person_2 = Person('God', 'Red')


# print(person_1.firstname, person_1.lastname)
# print(person_2.firstname, person_2.lastname)


class Point():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        self.__x = x

    def set_x(self, x):
        self.__x = x


point_10_20 = Point(10, 20)


# print(point_10_20.get_x(), point_10_20.get_y())


class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def set_price(self, price):
        if price <= 0:
            raise ValueError('Invalid price')
        self.price = price

    def get_price(self):
        return self.price


class OrderException(Exception):
    pass


class Order(object):
    def __init__(self, person):
        self.person = person
        self.products = []

    def add_products(self, product):
        if not isinstance(product, Product):
            raise OrderException('Это не продукт!\n{}'.format(type(product)))
        self.products.append(product)

    def get_total_price(self):
        return sum(p.get_price() for p in self.products)


# Статические свойства и методы


class Factory(object):
    instances = {}

    # @staticmethod
    @classmethod
    def get_instance(cls, name, *args, **kwargs):
        if name not in cls.instances:
            cls.instances[name] = cls(*args, **kwargs)
        return cls.instances[name]


print(Factory.get_instance('name1'),
      Factory.get_instance('name1'),
      Factory.get_instance('name2'))
