# -*- coding: utf-8 -*-
import os

import scrapy
from PIL import Image
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from NovelCharacters.items import ImageItem
from NovelCharacters.settings import IMAGES_STORE


class NovelcharactersPipeline(object):
    def process_item(self, item, spider):
        return item


class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 此方法在发送下载请求前调用(此方法本身就是求发送下载请求的)
        if isinstance(item, ImageItem):
            request_objs = super().get_media_requests(item, info)

            for request_obj in request_objs:
                request_obj.item = item
            return request_objs

    def file_path(self, request, response=None, info=None):
        # 此方法是在图片将要被存储时被调用,获取图片存储路径
        path = super().file_path(request, response, info)
        img_path = request.item.get('img_path')
        images_store = IMAGES_STORE
        name_path = os.path.join(images_store, img_path)
        image_path = name_path + '.jpg'
        return image_path



























    # def get_media_requests(self, item, info):
    #     if isinstance(item, ImageItem):  # 判断item是否为ImageItem类型
    #         print('---', item)
    #         for image_url in item['character_img']:
    #             if 'http' in image_url:
    #                 return scrapy.Request(url=image_url, meta={'item': item})
    #
    # def file_path(self, request, response=None, info=None):
    #     item = request.meta['item']
    #     print('item--', item)
    #     file_name = '{}.jpg'.format(item['img_path'])
    #     return file_name
    #
    # def item_completed(self, results, item, info):
    #     if isinstance(item, ImageItem):
    #         print('result', results, item)
    #         image_paths = [x['path'] for ok, x in results if ok]
    #         image_url = [x['url'] for ok, x in results if ok]
    #         if not image_paths:
    #             raise DropItem("Item contains no images")
    #         else:
    #             print(image_paths)
    #             if image_url == item['character_img']:
    #                 return item
    #             else:
    #                 raise DropItem("图片出错啦", image_url, item['character_img'])
    #     else:
    #         return item


