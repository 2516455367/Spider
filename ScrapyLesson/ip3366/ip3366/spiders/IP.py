# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup

from ip3366.items import Ip3366Item

n=0
class IpSpider(scrapy.Spider):
    name = 'IP'
    allowed_domains = ['ip3366.net']
    start_urls = ['http://www.ip3366.net/free/']

    def parse(self, response):
        selector = BeautifulSoup(response.text, 'lxml')
        list = selector.select('tbody tr')
        item = Ip3366Item()
        for tr in list:
            i_num = tr.select('td:nth-child(1)')
            port = tr.select('td:nth-child(2)')
            Http_type = tr.select('td:nth-child(4)')
            IP_dict = {}
            IP_dict[Http_type[0].text] = i_num[0].text + ':' + port[0].text
            item['IP_list'] = IP_dict
            yield item
        global n
        if n<1:
            next_page = selector.select('#listnav ul a:nth-child(9)')[0].attrs['href']
            if next_page:
                next_url = response.urljoin(next_page)
                n = n + 1
                print(next_url)
                yield scrapy.Request(url=next_url, callback=self.parse,dont_filter=True)
        else:
            try:
                next_page = selector.select('#listnav ul a:nth-child(11)')[0].attrs['href']
                if next_page != None:
                    next_url = response.urljoin(next_page)
                    n = n + 1
                    print(next_url)
                    yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)
            except:
                pass
