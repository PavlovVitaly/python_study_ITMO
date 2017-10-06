# Ввод и вывод

"""
Стандартный поток ввода
stdin(№0) -> input

Стандартный поток ввода
stdout(№1) -> print()

Стандартный поток ошибок
stderr(№2) -> ошибки интерпретатора (и те которые скидывает сам программист)

sys.stdin, sys.stdout, sys.stderr
"""

"""
Работа с файлами

open(filename, mode)

Режимы записи
w - перезапись
a - дозапись в конец
x - эксклюзивное создание файла (если файл создан, выдаст ошибку)

Режимы чтения
r - чтение (режим по-умолчанию)
w+, a+, x+, - чтение + запись

===
t -> open('out.txt', 'wt') - текстовый режим
b -> open('1.mp3', 'rb') - бинарный режим (возвращаются байтовые строки)

path.exist(filename) - существование файла
"""

f = open('out.txt', 'w')  # Дескриптор открытого файла.
f.write('123\n')
f.write('456')
f.writelines(['C', 'D'])
f.write('\rtest')
f.close()

f = open('out.txt', 'r')
print('Как прочитать файл в строку целиком')
content = f.read()
print(content)

print('Как прочитать файл в список')
f.seek(0)  # Смещение курсора в байтах относительно начала файла.
content = f.readlines()
print(content)

f.seek(0)
print('Как прочитать файл построчно')
line = f.readline()
print(line)
for line in f:
    print(line.strip())

f.seek(0)
print('Как прочитать из файла N байтов')
print(f.read(5))

print('Как узнать позицию курсора?')
print(f.tell())

f.close()

# Менеджер контекста
# Вместо try catch finally
with open('out.txt') as f1:
    content1 = f1.read()
    print(content1)

print(f1)
print(content1)
