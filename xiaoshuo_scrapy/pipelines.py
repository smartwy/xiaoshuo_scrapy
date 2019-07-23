# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request
from urllib.request import urlopen
# 当使用urllib模块访问https网站时，由于需要提交表单，
# 而python3默认是不提交表单的，所以这时只需在代码中加上以下代码即可
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from lxml import etree
import requests
requests.packages.urllib3.disable_warnings()  # 解决 verify=False时的报错，https没有证书验证

class XiaoshuoScrapyPipeline(object):
    def process_item(self, item, spider):
        # print(item['title'],item['href_url'])
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}
        req = request.Request(url=item['href_url'], headers=headers, method='GET')
        res = urlopen(req)
        res = res.read().decode()
        res = etree.HTML(res) # 构造一个xpath解析对象
        res = res.xpath('//*[@id="content"]/text()')
        txt = ''.join(res)
        dir_path = r'E:\python_project_dir\xiaoshuo_scrapy\sx_txt_dir'
        file_name = os.path.join(dir_path, item['title'] + '.txt')
        with open(file_name, 'w+') as fp:
            fp.write(txt)

        # hdata = requests.get(url=item['href_url'], verify=False)
        # html = etree.HTML(hdata.text) # etree.HTML():构造了一个XPath解析对象并对HTML文本进行自动修正
        # chapter = html.xpath('//*[@id="content"]/text()')
        # txt = ''.join(chapter)
        # dir_path = 'E:\\python_project_dir\\xiaoshou_txt\\xiaoshuo_chapter'
        # file_name = os.path.join(dir_path, item['title'] + '.txt')
        # with open(file_name, 'w+', encoding='utf-8') as fp:
        #     fp.write(txt)

        return item
