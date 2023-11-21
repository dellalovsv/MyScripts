import config
from funcs import ex_rates, telegram
from messages import rates_exchange as msg_re

from datetime import datetime as dt


def main():
    rates = ex_rates.CbRf().get_rates()
    if rates is not None:
        msg = msg_re.rate_now % (
            dt.now().strftime('%d.%m.%Y'),
            rates['USD'],
            rates['EUR'],
            rates['UAH'],
            rates['CNY'],
            rates['GBP']
        )
        telegram.sendMessage(msg, config.Telegram.admins)


if __name__ == '__main__':
    main()
