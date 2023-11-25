class Telegram(object):
    token = '942781206:AAEiozAlW4t-t30gCPP49wnSKCQzY1PJTYE'
    admins = [
        263007277
    ]
    urls = {
        'sendMessage': f'https://api.telegram.org/bot{token}/sendMessage'
    }


class Database(object):
    host = 'mysql'
    port = 3306
    user = 'dev'
    password = '12345678'
    db = 'da_system'
