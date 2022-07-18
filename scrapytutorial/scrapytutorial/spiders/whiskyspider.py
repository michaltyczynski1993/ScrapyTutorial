import scrapy


class WhiskySpider(scrapy.Spider):
    name = 'whisky'
    start_urls = ['https://www.whiskyshop.com/single-malt-scotch-whisky']

    def parse(self, response):
        for products in response.css('div.product-item-info'):
            yield {
                'name': products.css('span.price ::text').get(),
                'price': products.css('a.product-item-link ::text').get(),
                'link': products.css('a.product-item-link').attrib['href'],
            }
