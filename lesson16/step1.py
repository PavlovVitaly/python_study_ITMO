# ORM - Object Relational Mapping
# PonyORM
from datetime import date

from pony.orm import (Database, Required, Optional, Set, db_session, sql_debug, show, select)

db = Database()
sql_debug(True)


class Person(db.Entity):
    firstname = Required(str)
    lastname = Required(str)
    phone = Required(str)
    birthday = Optional(date)
    address = Optional('Address')


class Address(db.Entity):
    city = Required(str)
    street = Required(str)
    build = Required(str)
    flat = Required(str)
    persons = Set(Person)


db.bind('sqlite', filename=':memory:')
db.generate_mapping(create_tables=True)

with db_session:
    address = Address(city='spb', street='Lomonosova', build='9', flat='3404')
    person = Person(firstname='Ivan', lastname='Davis', phone='89147585458', address=address)
    person = Person(firstname='Ivan', lastname='Daviz', phone='89147784458')

with db_session:
    person = Person[1]  # Выборка по ПК.
    show(person)
    show(person.address)

with db_session:
    person = Person.get(lastname='Daviz')
    show(person)

    person = select(p for p in Person if p.firstname == 'Ivan')
    show(person)
