# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from urllib import request
import os


class DoutuPipeline(object):
    def process_item(self, item, spider):
        try:
            filename = 'D:\doutu\{}'.format(item['name']) + item['img_url'][-4:]
            if not os.path.exists(filename):
                buff = request.urlopen(item['img_url']).read()
                with open(filename, 'wb') as f:
                    f.write(buff)
            else:
                print('图片已经存在了！！！')
        except Exception as e:
            print(repr(e))
        return item
