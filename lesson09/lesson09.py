# Исключения


class CustomError(Exception):
    pass


try:
    n = int(input())
    raise CustomError('Что-то пошло не так.')
except ValueError:
    print('Не число')
except (ImportError, CustomError) as e:
    print(e)
