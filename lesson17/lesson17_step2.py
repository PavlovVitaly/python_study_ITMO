Person = type('Person', (object,), {
    'firstname': None,
    'lastname': None
})


def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname


setattr(Person, '__init__', __init__)

print(Person, type(Person))
p = Person('Jonathan', 'Davis')
print(p, type(p))


#  Метаклассы


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


# six - polyfill для метаклассов Python2 и Python3

class Config(metaclass=Singleton):
    # __metaclass__ = Singleton   # Python2
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
