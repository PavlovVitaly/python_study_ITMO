# Специальные свойства методы классов и объектов

class Singleton(object):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls, *args, **kwargs)
        return cls._instances[cls]


class Config(Singleton):
    def __init__(self):
        self.__config = {}

    def add(self, key, value):
        self.__config[key] = value

    def get(self, key):
        return self.__config.get(key)


config1 = Config()
config2 = Config()
print(config1 is config2)
print(config1, config2)

config1.add('host', 'localhost')
print(config1.get('host'))


class Product(object):
    """
    Продукт магазина
    """

    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return 'Str: Продукт "{}" стоимость {}'.format(self.title, self.price)

    def __repr__(self):
        return 'Product("{}", {})'.format(self.title, self.price)

    def __int__(self):
        return int(self.price)

    def __float__(self):
        return float(self.price)

    def __bool__(self):
        return bool(self.title and self.price)


class Cart(object):
    def __init__(self):
        self.__products = []

    def add(self, product):
        if not isinstance(product, Product):
            raise ValueError
        self.__products.append(product)

    def __len__(self):
        return len(self.__products)

    def __contains__(self, item):
        assert isinstance(item, Product)
        return item in self.__products

    def __setitem__(self, key, value):
        assert isinstance(value, Product)
        self.__products.insert(key, value)

    def __getitem__(self, item):
        return self.__products[item]

    def __delitem__(self, key):
        del self.__products[key]


print(Product.__name__)  # Имя класса.
print(Product.__class__)  # Имя метакласса.
print(Product.__module__)  # Имя модуля, в котором описан данный класс.
print(Product.__doc__)  # Строка документации.
print(Product.__bases__)  # Кортеж базовых классов.
print(Product.__dict__)  # Словарь атрибутов.

cart = Cart()

product = Product('Book', 999.9)
cart.add(product)

product2 = Product('PC', 9000000.1)
cart.add(product2)

print(product.__dict__)  # Сдоварь атрибутов объекта.
print(product.__class__)  # Класс на основе которого создан объект.
print(product.__class__.__name__)
print(product)

print(str(product))
print(repr(product))
print(type(eval(repr(product))))
print(int(product), float(product), bool(product))

print('Numbers of products:', len(cart))
print(product2 in cart)

chocolate = Product('chocolate', 250.99)
cognac = Product('Cognac', 45000.05)

cart[0] = chocolate
cart[1] = cognac

print(cart[1])


# Перегрузка опереторов


class Vector(object):
    __slots__ = ('x', 'y')
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        """Перегрузка оператора +"""
        assert isinstance(other, self.__class__)
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        """Перегрузка оператора -"""
        assert isinstance(other, self.__class__)
        x = self.x - other.x
        y = self.y - other.y
        return self.__class__(x, y)

    def __mul__(self, other):
        """Перегрузка оператора *"""
        assert isinstance(other, self.__class__)
        x = self.x * other.x
        y = self.y * other.y
        return self.__class__(x, y)

    def __gt__(self, other):
        """Перегрузка оператора >"""
        assert isinstance(other, self.__class__)
        return self.length > other.length

    def __ge__(self, other):
        """Перегрузка оператора >"""
        assert isinstance(other, self.__class__)
        return self.length >= other.length

    def __eq__(self, other):
        """Перегрузка оператора >"""
        assert isinstance(other, self.__class__)
        return self.length == other.length

    @property
    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


v1 = Vector(-3, 4)
v2 = Vector(-3, 6)
v3 = v1 + v2
v4 = v1 - v2
v5 = v1 * v2

print(v1)
print(v2)
print(v3)
print(v4)
print(v5)
print('Vector v1 > v2', v1 > v2)
print('Vector v1 < v2', v1 < v2)
print('Vector v1 = v2', v1 == v2)
print('Vector v1 >= v2', v1 >= v2)
print('Vector v1 <= v2', v1 <= v2)
