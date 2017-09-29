# Тип данных
a = 3
print(type(a))  # Определение типа данных

# Явное приведение типов
#   Дзен Питона
a = a + 1.5  # Неявное приведение типов
print(type(a))

a = str(a) + '2'  # Явное приведение типов
print(type(a))
print(a)

# Ссылки
lst = [1, 2, 3]
lst2 = lst
print(type(lst2))
lst = tuple(lst)
print(type(lst2))

# Конвертирование
print(int('0110', 2))

# Операторы

# Арифметические: + - * / %(остаток от деления) //(целочисленное деление) **(степень)
print(4 ** 0.5)

# Операторы сравнения: == != <>(неравенство) > < >= <=

# Опереторы присваивания:  = += -= *= /=

a = -3
print(a)
a = -a
print(a)

# Логические: and or not

# Принадлежности: in, not in
print(1 in lst2)

# Операторы тождественности: is, not is
lst = [1, 2, 3]
lst2 = [1, 2, 3]
print(lst == lst2)
print(lst is lst2)

# Непроверять None через ==, только через is (not is)!!!!!!!!!!!!!!!!

# Побитовые: & | ^(xor) ~ << >>

print(bool(0))
print(bool(''))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(set()))
