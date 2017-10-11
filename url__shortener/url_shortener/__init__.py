import os.path as Path
import sys

from url_shortener import storage

get_connection = lambda: storage.connect('shortener.sqlite')


def action_add():
    """добавит url-адрес"""
    url = input('\nВведите URL-адрес: ')
    with get_connection() as conn:
        short_url = storage.add_url(conn, url)

    if not url:
        return

    print('Короткий адрес: {}'.format(short_url))


def action_find():
    """Найти оригинальный url-адрес"""
    short_url = input('\nВведите короткий URL-адрес: ')

    if short_url:
        with get_connection() as conn:
            row = storage.find_url_by_short(conn, short_url)
        if row:
            url = row.get('original_url')
            print('Оригинальный URL-адрес: {}'.format(url))
        else:
            print('Короткий URL-адрес "{}" не существует'.format(short_url))


def action_find_all():
    """вывести все url-адреса"""
    with get_connection() as conn:
        rows = storage.find_all(conn)

    template = '{row[short_url]} - {row[original_url]} - {row[created]}'

    for row in rows:
        print(template.format(row=row))


def action_show_menu():
    """показать меню"""
    print("""
1. Добавить URL-адрес
2. Найти оригинальный URL-адрес
3. Найти все URL-адрес
m. Показать меню
q. Выйти""")


def action_exit():
    """выйти из программы"""
    sys.exit(0)  # от тысячи и выше


def main():
    creation_schema = Path.join(
        Path.dirname(__file__), 'schema.sql'
    )

    with get_connection() as conn:
        storage.initialize(conn, creation_schema)

    actions = {
        '1': action_add,
        '2': action_find,
        '3': action_find_all,
        'm': action_show_menu,
        'q': action_exit
    }

    action_show_menu()

    while True:
        cmd = input('\nВведите команду:')
        action = actions.get(cmd)
        if action:
            action()
        else:
            print('Неизвестная команда')
