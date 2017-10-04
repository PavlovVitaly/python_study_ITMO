"""
name - название пакета
version - версия
description - краткое описаниет пакета.
url - url-адрес сайта.
license - Лицензия (требуется версионная запись!).
author - имя автора.
author_email - почта автора.
packages - Пакетыб которые необходимо скопировать
            без рекурсии, необходимо указывать вложенность.
-------- конец обязательных параметров -----
py_modules - модули, которые необходимо скопировать.
install-requires - прямые зависимости пакета от других пакетов.
scripts - запускаемые из командной строки скрипты.
"""

from setuptools import setup

setup(
    name='mega-math',
    version='1.0.0',
    description='Collection of mathematical formulas',
    url='https://github.com/math-mega',
    license='Apache License 2.0',
    author='Pavlov Vitaly',
    author_email='pvs.mazilla@gmail.com',
    packages=[
        'mega_math'
    ]
)
