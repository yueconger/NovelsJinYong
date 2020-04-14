# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelcharactersItem(scrapy.Item):
    # define the fields for your item here like:
    book_name = scrapy.Field()
    character_url = scrapy.Field()
    character_img = scrapy.Field()

    character_name = scrapy.Field()
    # book_name = scrapy.Field()
    # book_name = scrapy.Field()
    # book_name = scrapy.Field()
    # book_name = scrapy.Field()
    # book_name = scrapy.Field()


class ImageItem(scrapy.Item):
    character_img = scrapy.Field()
    img_path = scrapy.Field()
    image_path = scrapy.Field()
