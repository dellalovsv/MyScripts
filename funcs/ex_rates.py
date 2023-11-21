from . import get_page

from bs4 import BeautifulSoup
from lxml import etree


class CbRf:
    def get_rates(self):
        url = 'https://cbr.ru/curreNcy_base/daily/'
        currency = {
            'USD': '//*[@id="content"]/div/div/div/div[3]/div/table/tbody/tr[15]/td[5]',
            'EUR': '//*[@id="content"]/div/div/div/div[3]/div/table/tbody/tr[16]/td[5]',
            'UAH': '//*[@id="content"]/div/div/div/div[3]/div/table/tbody/tr[38]/td[5]'
        }
        page = get_page(url)
        if page is not None:
            soup = BeautifulSoup(page.content, 'lxml')
            res = {}
            for item in currency:
                dom = etree.HTML(str(soup))
                res[item] = dom.xpath(currency[item])[0].text
                # res.append(dom.xpath(currency[item])[0].text)
            return res
        else:
            return None
