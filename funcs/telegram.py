import config

import requests


def sendMessage(msg: str = None, admins: list = None):
    for admin in admins:
        data = {
            'chat_id': admin,
            'text': msg,
            'parse_mode': 'HTML'
        }
        if requests.get(config.Telegram.urls['sendMessage'], data=data).status_code != 200:
            return False
    return True
