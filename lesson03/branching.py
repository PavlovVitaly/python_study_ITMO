# Ветвление
a = 1
b = 2

if a > b:
    # pass # пустая инструкция т.к. нельзя оставить пустую реализацию
    print('a > b')
elif a == b:
    print('a == b')
else:
    print('a <= b')

# Тернальный оператор
# условие ? истина : ложь
flag = True
v = 5 if flag else 'Hello'
print(v)
