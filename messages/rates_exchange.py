from . import ico_cash, ico_number_1, ico_number_10, ico_currency


rate_now = (f'{ico_cash} <b>Текущий курс валют на %s</b>:\n'
            '<b>ЦБ РФ</b>:\n'
            f'USD {ico_number_1}: <b>%s</b> {ico_currency["RUB"]}\n'
            f'EUR {ico_number_1}: <b>%s</b> {ico_currency["RUB"]}\n'
            f'UAH {ico_number_10}: <b>%s</b> {ico_currency["RUB"]}\n'
            f'CNY {ico_number_1}: <b>%s</b> {ico_currency["RUB"]}\n'
            f'GBP {ico_number_1}: <b>%s</b> {ico_currency["RUB"]}')
