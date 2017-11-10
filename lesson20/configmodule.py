class Config(object):
    SECRET_KEY = 'Random string'
    WTF_CSRF_SECRET_KEY = 'WTF secret key'
    DB = {
        'type': 'sqlite',
        'dbname': 'shop.sqlite'
    }
