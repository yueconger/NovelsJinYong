# -*- coding: utf-8 -*-
import scrapy
from NovelCharacters.items import NovelcharactersItem, ImageItem


class WuxiaSpider(scrapy.Spider):
    name = 'wuxia'
    allowed_domains = ['jinyongwang.com']
    start_urls = ['http://jinyongwang.com/']

    def start_requests(self):
        data_name_list = ['renwu', 'wugong', 'menpai']   # 人物,武功,门派
        url_ori = 'http://www.jinyongwang.com/data/{}/'
        url = url_ori.format(data_name_list[0])
        yield scrapy.Request(
            url=url,
            callback=self.parse
        )

    def parse(self, response):
        # item = NovelcharactersItem()
        item = {}

        booklist = response.xpath('//div[@class="booklist"][1]')
        book_name_list = booklist.xpath('./h2[@class="dataname"]')
        characters_list = booklist.xpath('./div[@class="datapice"]')
        for i in range(len(book_name_list)):
            book_name = book_name_list[i].xpath('./span/text()').extract_first()
            book_character_list = characters_list[i].xpath('./a')
            item['book_name'] = book_name

            for book_character in book_character_list:
                img_item = ImageItem()

                character_url = book_character.xpath('./@href').extract_first()
                character_url = response.urljoin(character_url)
                character_img = book_character.xpath('./img/@src').extract_first()
                character_name = book_character.xpath('./text()').extract_first()
                if character_img:
                    character_img = response.urljoin(character_img)
                    character_img = character_img.replace('_120.jpg', '.jpg')
                    img_item['character_img'] = [character_img]
                    img_item['img_path'] = '_'.join([book_name, character_name])
                    yield img_item
                else:
                    character_img = ''
                item['character_url'] = character_url
                item['character_img'] = character_img
                item['character_name'] = character_name


                # yield scrapy.Request(
                #     url=character_url,
                #     callback=self.characters_parse,
                #     meta={'item': item}
                # )

    def characters_parse(self, response):
        item = response.meta['item']
        pass
