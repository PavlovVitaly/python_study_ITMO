"""
SQL - Structured Query Language
- DDL - Data Definition Language
- DML - Data Manipulation Language
СУБД - Система Управления Базами Данных
Primary Key (Первичный ключ)
    Уникальный идентификатор
    Может быть int, может быть str.
    Может быть составной (суррогатный).
Foreign Key (Внешний ключ)

Алгоритм работы с БД:
1. Установка соединения .connect()
2. Создание объекта курсора conn.cursor()
3. Выполнение SQL-запросов cursor.execute()
4. Если запрос изменяет данные/структуру зафиксировать изменения conn.commit()
4. Если запрос на выборку данных
    4.1 разобрать данные (fetch*)
"""

# SQLite3
import sqlite3

# conn = sqlite3.connect(':memory:')        # в оперативной памяти
conn = sqlite3.connect('users.sqlite')
cursor = conn.cursor()
sql = """
CREATE TABLE IF NOT EXISTS user(
id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
)
"""
cursor.execute(sql)
conn.commit()
sql = """
INSERT INTO user (
first_name, last_name)
VALUES(
?, ?
) 
"""
# ? - placeholder

cursor.execute(sql, ('Вася', 'Пупкин'))
conn.commit()

sql = """
SELECT 
id, first_name, last_name, created
FROM
user
"""
cursor.execute(sql)
users = cursor.fetchall()
print(users)
conn.close()

with sqlite3.connect('users.sqlite') as conn:
    cursor = conn.execute(sql)
    users = cursor.fetchall()
    print(users)
