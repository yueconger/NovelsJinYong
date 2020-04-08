# -*- coding: utf-8 -*-
import scrapy


class WuxiaSpider(scrapy.Spider):
    name = 'wuxia'
    allowed_domains = ['jinyongwang.com']
    start_urls = ['http://jinyongwang.com/']

    def start_requests(self):
        data_name_list = ['renwu', 'wugong', 'menpai']
        url_ori = 'http://www.jinyongwang.com/data/{}/'
        url = url_ori.format(data_name_list[0])
        yield scrapy.Request(
            url=url,
            callback=self.parse
        )

    def parse(self, response):
        print('-'* 50)
        print(response.request.headers['User-Agent'])