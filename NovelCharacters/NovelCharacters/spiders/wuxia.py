# -*- coding: utf-8 -*-
import scrapy


class WuxiaSpider(scrapy.Spider):
    name = 'wuxia'
    allowed_domains = ['jinyongwang.com']
    start_urls = ['http://jinyongwang.com/']

    def parse(self, response):
        pass
