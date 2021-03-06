import os.path as Path
import sys
from collections import OrderedDict, namedtuple

from url_shortener import storage

get_connection = lambda: storage.connect('shortener.sqlite')

Action = namedtuple('Action', ['func', 'name'])
actions = OrderedDict()


def menu_action(cmd, name):
    def decorator(func):
        actions[cmd] = Action(func=func, name=name)
        return func

    return decorator


@menu_action('1', 'Добавить URL-адрес')
def action_add():
    """добавит url-адрес"""
    url = input('\nВведите URL-адрес: ')
    with get_connection() as conn:
        short_url = storage.add_url(conn, url)

    if not url:
        return

    print('Короткий адрес: {}'.format(short_url))


@menu_action('2', 'Найти оригинальный url-адрес')
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


@menu_action('3', 'Вывести все url-адреса')
def action_find_all():
    """вывести все url-адреса"""
    with get_connection() as conn:
        rows = storage.find_all(conn)

    template = '{row[short_url]} - {row[original_url]} - {row[created]}'

    for row in rows:
        print(template.format(row=row))


@menu_action('m', 'Показать меню"')
def action_show_menu():
    """показать меню"""
    menu = []
    for cmd, action in actions.items():
        menu.append('{}. {}'.format(cmd, action.name))
    print('\n'.join(menu))


@menu_action('q', 'Выйти из программы')
def action_exit():
    """выйти из программы"""
    sys.exit(0)  # от тысячи и выше


def main():
    creation_schema = Path.join(
        Path.dirname(__file__), 'schema.sql'
    )

    with get_connection() as conn:
        storage.initialize(conn, creation_schema)


    action_show_menu()

    while True:
        cmd = input('\nВведите команду:')
        action = actions.get(cmd)
        if action:
            action.func()
        else:
            print('Неизвестная команда')
