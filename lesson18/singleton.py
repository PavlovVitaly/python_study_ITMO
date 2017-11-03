# Design Patterns


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Config(object):
    def __init__(self):
        self.__config = {}

    def __setitem__(self, key, value):
        self.__config[key] = value

    def __getitem__(self, item):
        return self.__config.get(item)


config1 = Config()
config2 = Config()

print(config1 is config2)
