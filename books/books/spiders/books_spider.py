import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        common_part = '//div/div/div/div/section/div/{}'
        for book in response.xpath(common_part.format('ol/li')):
            yield {'title': book.xpath('./article/h3/a/@title').extract_first()}

        next_page_url = response.xpath(common_part.format('div/ul/li[@class="next"]/a/@href')).extract_first()
        if next_page_url is not None:
            yield response.follow(next_page_url)


if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl(BooksSpider)
    process.start()
