# -*- coding: utf-8 -*-
import scrapy


class BooksSpiderSpider(scrapy.Spider):
    name = 'books_spider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        pass
