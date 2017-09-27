print("Hello, world!")  # однострочный комментарий
"""
    многострочный
    комментарий
"""
# pep8

is_student = True

name = input('Введите имя: ')
print("Hello,", name, "!")

# Тип данных:
#   - Скалярные типы:
#       + bool
#       + int
i1 = 666
i2 = 0x59
i3 = 0b101010  # бинарная сс
i4 = 0o255  # восьмеричная сс

#       + float
f1 = 1.23
f2 = 12e-3

#       + str
s1 = 'Some string'
s2 = "Some string"
s3 = r'Raw string'  # Сырая строка
s4 = u'Hello'  # unicode string для обратной совместимости с python2

#       + bytes - байтовая строка
s5 = b"byte's string"

s6 = '''

'''  # с сохранением формата
s7 = """
    1.  lklk
"""  # с сохранением формата

#       + комплексные числа - complex
c1 = 3.14j

# pyitmo группа вк

#   - Структурированные (сложные) типы данных
#       + tuple - кортеж
t1 = (1,)  # кортеж из одного элемента
t2 = (True, 6, 1.2, 'String', (1, 2, 3))
print(t2[1])  # обращение одинаковое в tuple, list, set.

#       + list
lst1 = [[1], [2], 3, False, ()]
print(lst1[0], [0])  # элемет вложенного списка

#       + set - элементы не повторяются
set1 = {1, 2, 3, 'string'}
set2 = set()  # пустое множество

#       + dict - словари (не сохраняет порядок эл-тов)
d0 = {}  # пустой словарь, не множество!
d = {
    'id': 1,
    'name': 'Jone',
    'id_student': True,
    'skills': ('python', 'linux')
}

#       + object

#       + Специальные типы
#           * None - пустой тип
a = None