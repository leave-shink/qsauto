# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from qsauto.items import QsautoItem

class WensuenSpider(CrawlSpider):
    name = 'wensuen'
    allowed_domains = ['qiushibaike.com']
    # start_urls = ['http://qiushibaike.com/']
    def start_requests(self):
        ua = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6721.400 QQBrowser/10.2.2243.400'}
        yield Request('http://qiushibaike.com/', headers=ua)

    rules = (
        Rule(LinkExtractor(allow=r'article'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = QsautoItem()
        i['content'] = response.xpath('//div[@class="content"]/text()').extract()
        i['link'] = response.xpath('//link[@rel="canonical"]/@href').extract()
        print(i['content'])
        print(i['link'])
        return i
