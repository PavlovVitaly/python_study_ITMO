# Запускаемый файл

import sys

# Импорт модуля целиком
import lesson05.mega_math.area_of_shapes as AREA

# Второй вариант
# Третий вариант
# Четвертый вариант
# from  area_of_shapes import *       # Лучше не использовать.


print(
    AREA.calculate_area_of_rectangle(1, 1)
)

print(dir(AREA))
print(sys.path)  # а также PYTHONPATH

AREA.sss = 2

print(
    AREA.calculate_area_of_rectangle(1, 1)
)

AREA.sss = 2

# Повторного импорта модуля не будет
# __pycashe__
# Запускаемый файл никогда не компилируется, его лучше делать меньше.
# Есть компиляция с оптимизацией (-O).

print(__name__)  # Имя модуля, если запускаемый,  то имя __main__ .

if __name__ == '__main__':
    print(
        AREA.calculate_area_of_square(2)
    )

# https://docs.python.org/3/library/index.html
