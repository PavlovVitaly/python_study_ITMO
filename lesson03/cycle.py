# Цикл
i = 1
summa = 0

while i < 10:
    summa += i
    i += 1

while i:
    if i == 10:
        break
    elif i == 8:
        i += 1
        continue
    i += 1

for i in range(10, 20, 2):
    print(i, end=', ')
print()

for i in range(10, 20):
    print(i, end=', ')
print()

for i in range(10):
    print(i, end=', ')
print()

d = {
    'id': 1,
    'name': 'Linus Torvalds'
}

for key, value in d.items():
    print(key, value)
