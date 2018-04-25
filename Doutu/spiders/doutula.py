import scrapy
from Doutu.items import DoutuItem


class Doutu(scrapy.Spider):
    name = 'doutu'
    allowed_domains = ['doutula.com']
    start_urls = ['http://www.doutula.com/photo/list/?page={}'.format(i) for i in range(1, 10)]

    def parse(self, response):
        print('========>')
        i = 0
        for content in response.xpath('//*[@id="pic-detail"]/div/div[2]/div[2]/ul/li/div/div/a'):
            # 分别处理每个图片，取出名称及地址
            item = DoutuItem()
            item['img_url'] = content.xpath('//img/@data-original').extract()[i]
            item['name'] = content.xpath('//p/text()').extract()[i]
            i += 1
            # 返回爬取到的信息
            yield item
        print('<========')
