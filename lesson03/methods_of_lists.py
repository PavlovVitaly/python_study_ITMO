result = []

for i in range(10):
    result.append(str(i))  # добавить в список

print(str(result))

result = ''.join(result)  # список в строку
print(result)

s = 'Hello, Python!'
s = list(s)
s[1] = '#'
s = ''.join(s)  # '' разделитель
print(s)
print(','.join(s))

# Списки не быстрые

lst = [100, 200, 1, 3]
print(lst)
print(lst.sort())
