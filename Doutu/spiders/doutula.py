import os
import scrapy
from Doutu.items import DoutuItem
from urllib import request


class Doutu(scrapy.Spider):
    name = 'doutu'
    allowed_domains = ['doutula.com']
    start_urls = ['http://www.doutula.com/photo/list/?page={}'.format(i) for i in range(1, 10)]

    def parse(self, response):
        i = 0
        print('========>')
        for content in response.xpath('//*[@id="pic-detail"]/div/div[2]/div[2]/ul/li/div/div/a'):
            items = DoutuItem()
            items['img_url'] = content.xpath('//img/@data-original').extract()[i]
            items['name'] = content.xpath('//p/text()').extract()[i]
            i += 1
            try:
                filename = 'D:\doutu\{}'.format(items['name']) + items['img_url'][-8:-4]
                if not os.path.exists(filename):
                    buff = request.urlopen(items['img_url']).read()
                    with open(filename, 'wb') as f:
                        f.write(buff)
                else:
                    print('图片已经存在了！！！')
            except Exception as e:
                print(repr(e))

            yield items

        print('<========')
