class Person(object):
    def __init__(self):
        self.username = None


person = Person()
print(person.username)
person.username = 'New name.'
print(person.username)
person.lastname = 'New last name'
print(person.lastname)

# hasattr(o, attr)   # Проверяет что атрибут существует.
# getattr(o, attr, default)   # Получает значение атрибута.
# setattr(o, attr, val)   # Устанавливает значение атрибута
# delattr(o, attr)   # Удаляет атрибут

print(hasattr(person, 'age'))
print(getattr(person, 'age', 0))
print(hasattr(person, 'age') and getattr(person, 'age'))

setattr(person, 'age', 45)
print(getattr(person, 'age'))
