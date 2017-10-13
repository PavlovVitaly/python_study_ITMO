import sqlite3

from .converter import convert, inverse

SQL_SELECT_ALL = """
    SELECT
        id, original_url, short_url, created
    FROM
      shortener
"""

SQL_SELECT_URL_BY_PK = SQL_SELECT_ALL + " WHERE id = ?"

SQL_SELECT_URL_BY_ORIGINAL = SQL_SELECT_ALL + " WHERE original_url = ?"

SQL_SELECT_URL_BY_SHORT = SQL_SELECT_ALL + " WHERE short_url = ?"

SQL_INSERT_URL = """
    INSERT INTO shortener (original_url) VALUES (?)
"""

SQL_UPDATE_SHORT_URL = """
    UPDATE shortener SET short_url = ? WHERE id = ? 
"""


def dict_factory(cursor, row):
    d = {}

    print("==>> Raw", row)
    print('==>>', cursor.description)

    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]

    return d


def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'
    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory
    return conn


def initialize(conn, creation_schema):
    with conn, open(creation_schema) as f:  # просто with не закроет соединение, но сделает ROLLBACK, либо COMMIT.
        conn.executescript(f.read())


def add_url(conn, url, domain=''):
    """Добавляет новый url-адрес в бд"""
    url = url.rstrip('/')

    if not url:
        # Здесь должна быть ошибка
        print('URL can not be empty!')
        return

    with conn:
        found = find_url_by_original(conn, url)

        if found:
            return found.get('short_url')
        cursor = conn.execute(SQL_INSERT_URL, (url,))
        pk = cursor.lastrowid  # последний сгенерированный запросом insert ЗЛ
        short_url = '{}/{}'.format(domain.strip('/'),
                                   convert(pk))

        conn.execute(SQL_UPDATE_SHORT_URL, (short_url, pk))

        return short_url


def find_all(conn):
    """Возвращает все URL-адреса из базы"""
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
        return cursor.fetchall()


def find_url_by_pk(conn, pk):
    """Возвращает все URL-адреса по первичному ключу"""
    with conn:
        cursor = conn.execute(SQL_SELECT_URL_BY_PK, (pk,))
        return cursor.fetchone()


def find_url_by_short(conn, short_url):
    """Возвращает все URL-адреса  по короткому URL-у"""
    short_url = short_url.rsplit('/', 1).pop()
    pk = inverse(short_url)
    return find_url_by_pk(conn, pk)


def find_url_by_original(conn, original_url):
    """Возвращает все URL-адреса  по оригинальному URL-у"""
    original_url = original_url.strip('/')

    with conn:
        cursor = conn.execute(SQL_SELECT_URL_BY_ORIGINAL,
                              (original_url,))
        return cursor.fetchone()
