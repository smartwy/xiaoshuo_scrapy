# -*- coding: utf-8 -*-
import scrapy
from xiaoshuo_scrapy.items import XiaoshuoTxtItem

class XiaoshuoSpider(scrapy.Spider):
    name = 'xs'
    allowed_domains = ['biqudu.net']
    start_urls = ['https://www.biqudu.net/2_2970/']

    def parse(self, response):
        html = XiaoshuoTxtItem()
        alllist = response.xpath('//div[@class="box_con"]/div/dl/dd')
        # title = response.xpath('//*[@id="list"]/dl/dd/a/text()') # 获取章节名
        # href = response.xpath('//*[@id="list"]/dl/dd/a/@href') # 获取章节内容
        for data in alllist:
            # print(data)
            title = data.xpath('./a/text()').extract()[0]
            href = data.xpath('./a/@href').extract()[0]
            # print(title, href)
            html['title'] = title
            href = 'https://www.biqudu.net/' + href
            html['href_url'] = href
            yield html
        # return html
