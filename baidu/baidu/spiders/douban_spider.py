# -*- coding: utf-8 -*-
import scrapy


class DoubanSpiderSpider(scrapy.Spider):
    # 这里是爬虫的名字
    name = 'douban_spider'
    # 允许的域名
    allowed_domains = ['www.sihongedu.com']
    # 入口url,扔到调度器里面去
    start_urls = ['https://www.sihongedu.com/']

    def parse(self, response):
        print(response.text)
