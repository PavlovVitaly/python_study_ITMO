import sqlite3

SQL_SELECT_ALL = """
    SELECT
        id, original_url, short_url, created
    FROM
      shortener
"""

SQL_SELECT_URL_BY_PK = SQL_SELECT_ALL + " WHERE id = ?"

SQL_SELECT_URL_BY_ORIGINAL = SQL_SELECT_ALL + " WHERE original_url = ?"

SQL_SELECT_URL_BY_SHORT = SQL_SELECT_ALL + " WHERE short_url = ?"

SELECT_INSERT_URL = """
    INSERT INTO shortener (original_url) VALUES (?)
"""

SQL_UPDATE_SHORT_URL = """
    UPDATE shortener SET shorter = ? WHERE id = ? 
"""


def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'
    # вставка кода будет
    conn = sqlite3.connect(db_name)
    return conn


def initialize(conn, creation_schema):
    with conn, open(creation_schema) as f:  # просто with не закроет соединение, но сделает ROLLBACK, либо COMMIT.
        conn.executescript(f.read())


def add_url(conn, url, domain=''):
    """Добавляет новый url-адрес в бд"""


def find_all(conn):
    """Возвращает все URL-адреса из базы"""


def find_url_by_pk(conn, pk):
    """Возвращает все URL-адреса по первичному ключу"""


def find_url_by_short(conn, short_url):
    """Возвращает все URL-адреса  по короткому URL-у"""


def find_url_by_original(conn, original_url):
    """Возвращает все URL-адреса  по оригинальному URL-у"""
