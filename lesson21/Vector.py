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
