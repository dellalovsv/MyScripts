from . import get_page

from bs4 import BeautifulSoup
from lxml import etree


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
