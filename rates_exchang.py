import config
from funcs import ex_rates, telegram
from messages import rates_exchange as msg_re

from datetime import datetime as dt


def main():
    cb_rates = ex_rates.CbRf().get_rates()
    banki_ru = ex_rates.BankiRU().get_rates()
    if cb_rates is not None:
        msg = msg_re.rate_now % (
            dt.now().strftime('%d.%m.%Y'),
            cb_rates['USD'],
            cb_rates['EUR'],
            cb_rates['UAH'],
            cb_rates['CNY'],
            cb_rates['GBP'],
            banki_ru['USD'][0],
            banki_ru['USD'][1],
            banki_ru['EUR'][0],
            banki_ru['EUR'][1],
            banki_ru['UAH'][0],
            banki_ru['UAH'][1],
            banki_ru['CNY'][0],
            banki_ru['CNY'][1],
            banki_ru['GBP'][0],
            banki_ru['GBP'][1],
        )
        telegram.sendMessage(msg, config.Telegram.admins)


if __name__ == '__main__':
    main()
