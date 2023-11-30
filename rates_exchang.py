import config
from funcs import ex_rates, telegram
from messages import rates_exchange as msg_re

from datetime import datetime as dt


def main():
    cb_rates = ex_rates.CbRf().get_rates()
    banki_ru = ex_rates.BankiRU().get_rates()
    if cb_rates is not None:
        for cb_rate in cb_rates:
            if cb_rates[cb_rate] == '—':
                cb_rates[cb_rate] = 0
        for bank_ru in banki_ru:
            if banki_ru[bank_ru][0] == '—':
                banki_ru[bank_ru][0] = 0
            if banki_ru[bank_ru][1] == '—':
                banki_ru[bank_ru][1] = 0
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
        ex_rates.save_now_rates([float(str(cb_rates['USD']).replace(",", ".")),
                                 float(str(cb_rates['EUR']).replace(',', '.')),
                                 float(str(cb_rates['UAH']).replace(',', '.')),
                                 float(str(cb_rates['CNY']).replace(',', '.')),
                                 float(str(cb_rates['GBP']).replace(',', '.'))],
                                [float(str(banki_ru['USD'][0]).replace(',', '.').split(' ')[0]),
                                 float(str(banki_ru['USD'][1]).replace(',', '.').split(' ')[0]),
                                 float(str(banki_ru['EUR'][0]).replace(',', '.').split(' ')[0]),
                                 float(str(banki_ru['EUR'][1]).replace(',', '.').split(' ')[0]),
                                 float(str(banki_ru['UAH'][0]).replace(',', '.').split(' ')[0]),
                                 float(str(banki_ru['UAH'][1]).replace(',', '.').split(' ')[0]),
                                 float(str(banki_ru['CNY'][0]).replace(',', '.').split(' ')[0]),
                                 float(str(banki_ru['CNY'][1]).replace(',', '.').split(' ')[0]),
                                 float(str(banki_ru['GBP'][0]).replace(',', '.').split(' ')[0]),
                                 float(str(banki_ru['GBP'][1]).replace(',', '.').split(' ')[0])])


if __name__ == '__main__':
    main()
