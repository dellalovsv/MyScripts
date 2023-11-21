import config
from funcs import ex_rates, telegram
from messages import rates_exchange as msg_re

from datetime import datetime as dt


def main():
    cb_rates = ex_rates.CbRf().get_rates()
    if cb_rates is not None:
        msg = msg_re.rate_now % (
            dt.now().strftime('%d.%m.%Y'),
            cb_rates['USD'],
            cb_rates['EUR'],
            cb_rates['UAH'],
            cb_rates['CNY'],
            cb_rates['GBP']
        )
        telegram.sendMessage(msg, config.Telegram.admins)


if __name__ == '__main__':
    main()
