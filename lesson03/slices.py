lst = list(range(1, 20))
print(lst)
print(lst[4])
print(lst[4:7])  # последняя позиция не включается (по 7-ой эл-т не включая 7-ой)
print(lst[4:])
print(lst[:7])
print(lst[:])  # выдает новый список (копия по значению)
print(lst[1:11:2])
print(lst[::2])  # нечетные
print(lst[1::2])  # четные
print(lst[-5])
print(lst[-5:])
print(lst[-5:-3])
print(lst[-5::-1])

s = 'Hello, Python'
print(s[::-1])
print(s[:5])
print(s[::2])
