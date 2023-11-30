from . import get_page, dt, query

from bs4 import BeautifulSoup
from lxml import etree


def get_last_rates():
    try:
        sql = (f'select cb_rf_usd_sale, cb_rf_eur_sale, cb_rf_uah_sale, cb_rf_cny_sale, cb_rf_gbp_sale '
               f'banki_ru_moscow_usd_purchase, banki_ru_moscow_usd_sale, '
               f'banki_ru_moscow_eur_purchase, banki_ru_moscow_eur_sale, '
               f'banki_ru_moscow_uah_purchase, banki_ru_moscow_uah_sale, '
               f'banki_ru_moscow_cny_purchase, banki_ru_moscow_cny_sale, '
               f'banki_ru_moscow_gbp_purchase, banki_ru_moscow_gbp_sale from rates_ex where date=%s limit 1')
        res = query(sql, dt.get_yesterday()[0])
        if res is not None and res is not False and len(res) > 0:
            return res[0]
    except Exception as e:
        print(f'funcs.ex_rates.get_last_rates (ERROR): {e}')
        return None


def save_now_rates(data_cb: list[float], data_banki_ru: list[float]) -> bool:
    """
    Запись текущих курсов валют.\n
    Формат переменных: data_cb[usd, eur, uah, cny, gbp]; data_bank_ru[usd_purchase, usd_sale, eur_purchase, eur_sale,
    uah_purchase, uah_sale, cny_purchase, cny_sale, gbp_purchase, gbp_sale]
    """
    try:
        sql = ('insert into rates_ex (cb_rf_usd_sale, cb_rf_eur_sale, cb_rf_uah_sale, cb_rf_cny_sale, cb_rf_gbp_sale, '
               'banki_ru_moscow_usd_purchase, banki_ru_moscow_usd_sale, '
               'banki_ru_moscow_eur_purchase, banki_ru_moscow_eur_sale, '
               'banki_ru_moscow_uah_purchase, banki_ru_moscow_uah_sale, '
               'banki_ru_moscow_cny_purchase, banki_ru_moscow_cny_sale, '
               'banki_ru_moscow_gbp_purchase, banki_ru_moscow_gbp_sale) values ('
               '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)')
        res = query(
            sql,
            data_cb[0], data_cb[1], data_cb[2], data_cb[3], data_cb[4],
            data_banki_ru[0], data_banki_ru[1], data_banki_ru[2], data_banki_ru[3], data_banki_ru[4],
            data_banki_ru[5], data_banki_ru[6], data_banki_ru[7], data_banki_ru[8], data_banki_ru[9],
            commit=True
        )
        if res:
            return True

        return False
    except Exception as e:
        print(f'funcs.ex_rates.save_now_rates (ERROR): {e}')
        return False


def get_compare(data_cb: list[float], data_banki_ru: list[float]):
    last_rates = get_last_rates()
    if last_rates is not None and last_rates is not False and len(last_rates) > 0:
        res_cb = []
        res_banki = []

    return None


class CbRf:
    def get_rates(self):
        url = 'https://cbr.ru/curreNcy_base/daily/'
        currency = {
            'date': '//*[@id="UniDbQuery_form"]/div/div/div/div/button',
            'USD': '//*[@id="content"]/div/div/div/div[3]/div/table/tbody/tr[15]/td[5]',
            'EUR': '//*[@id="content"]/div/div/div/div[3]/div/table/tbody/tr[16]/td[5]',
            'UAH': '//*[@id="content"]/div/div/div/div[3]/div/table/tbody/tr[38]/td[5]',
            'CNY': '//*[@id="content"]/div/div/div/div[3]/div/table/tbody/tr[24]/td[5]',
            'GBP': '//*[@id="content"]/div/div/div/div[3]/div/table/tbody/tr[39]/td[5]'
        }
        page = get_page(url)
        if page is not None:
            soup = BeautifulSoup(page.content, 'lxml')
            res = {}
            for item in currency:
                dom = etree.HTML(str(soup))
                res[item] = dom.xpath(currency[item])[0].text
            return res
        else:
            return None


class BankiRU:
    def get_rates(self):
        urls = {
            'USD': 'https://www.banki.ru/products/currency/cash/usd/moskva/',
            'EUR': 'https://www.banki.ru/products/currency/cash/eur/moskva/',
            'UAH': 'https://www.banki.ru/products/currency/cash/uah/moskva/',
            'CNY': 'https://www.banki.ru/products/currency/cash/cny/moskva/',
            'GBP': 'https://www.banki.ru/products/currency/cash/gbp/moskva/'
        }
        xpath = {
            'purchase': '/html/body/div/div[2]/div[1]/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/section/div/'
                        'div/div/div[3]/div/div/div[2]/div[1]/div/div[2]',
            'sale': '/html/body/div/div[2]/div[1]/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/section/div/div/'
                    'div/div[3]/div/div/div[2]/div[2]/div/div/div[2]'
        }
        res = {}
        for url in urls:
            page = get_page(urls[url])
            if page.status_code == 200:
                soup = BeautifulSoup(page.content, 'lxml')
                dom = etree.HTML(str(soup))
                purchase = dom.xpath(xpath['purchase'])[0].text
                sale = dom.xpath(xpath['sale'])[0].text
                res[url] = [purchase, sale]
            else:
                return None
        return res
